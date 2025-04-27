# Group B-5 Write Python program to implement CNN object detection. Discuss numerous performance evaluation metrics for evaluating the object detecting algorithms' performance.
import tensorflow as tf
import numpy as np
import cv2

# Create a minimal CNN model for object detection
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

# Create a simple detection head
x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)

# Output layers: class and bounding box
class_output = tf.keras.layers.Dense(1, activation='sigmoid', name='class')(x)
box_output = tf.keras.layers.Dense(4, name='box')(x)

# Create model
model = tf.keras.Model(inputs=base_model.input, outputs=[class_output, box_output])
model.compile(optimizer='adam', loss={'class': 'binary_crossentropy', 'box': 'mse'})

# Function to detect objects in an image
def detect_object(image_path, threshold=0.5):
    # Load and preprocess image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255.0
    img = np.expand_dims(img, axis=0)
    
    # Run prediction
    class_pred, box_pred = model.predict(img)
    
    # Return predictions over threshold
    detections = []
    for i, conf in enumerate(class_pred):
        if conf[0] >= threshold:
            detections.append((box_pred[i], conf[0]))
    
    return detections

# Calculate IoU (Intersection over Union)
def calculate_iou(box1, box2):
    # Calculate intersection area
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[0] + box1[2], box2[0] + box2[2])
    y2 = min(box1[1] + box1[3], box2[1] + box2[3])
    
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    
    # Calculate union area
    box1_area = box1[2] * box1[3]
    box2_area = box2[2] * box2[3]
    union = box1_area + box2_area - intersection
    
    return intersection / union if union > 0 else 0

# Evaluate detection performance
def evaluate_detection(pred_boxes, gt_boxes, iou_threshold=0.5):
    tp = fp = 0
    fn = len(gt_boxes)
    
    for pred_box, _ in pred_boxes:
        best_iou = 0
        best_gt_idx = -1
        
        for i, gt_box in enumerate(gt_boxes):
            iou = calculate_iou(pred_box, gt_box)
            if iou > best_iou:
                best_iou = iou
                best_gt_idx = i
        
        if best_iou >= iou_threshold:
            tp += 1
            fn -= 1
        else:
            fp += 1
    
    # Calculate metrics
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    
    return {'precision': precision, 'recall': recall, 'f1_score': f1}
