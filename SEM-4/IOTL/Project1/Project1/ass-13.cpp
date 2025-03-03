//13. Write a program using piezo element and use it to play a tune after someone knocks

const int buzzer = A1; // Buzzer connected to analog pin A1
const int knockSensor = A0; // Piezo sensor connected to analog pin A0
const int threshold = 400; // Threshold value to detect knocks

void setup() {
    pinMode(buzzer, OUTPUT); // Set the buzzer pin as OUTPUT
}

void loop() {
    // Read the sensor value
    int sensorReading = analogRead(knockSensor);

    // Check if the sensor reading is greater than the threshold
    if (sensorReading >= threshold) {
        // Generate tones to play
        tone(buzzer, 261); // Play note C
        delay(200);
        noTone(buzzer);

        tone(buzzer, 293); // Play note D
        delay(200);
        noTone(buzzer);

        tone(buzzer, 329); // Play note E
        delay(200);
        noTone(buzzer);

        tone(buzzer, 349); // Play note F
        delay(200);
        noTone(buzzer);

        tone(buzzer, 392); // Play note G
        delay(200);
        noTone(buzzer);
    }

    delay(100); // Delay to avoid overloading the serial port buffer
}
