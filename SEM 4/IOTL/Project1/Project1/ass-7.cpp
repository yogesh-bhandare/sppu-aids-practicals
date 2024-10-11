//7. Create a program so that when the user enters ‘b’ the green light blinks, ‘g’ the green light is illuminated ‘y’ the yellow light is illuminated and ‘r’ the red light is illuminated

// Pins connected to the LEDs
const int greenLedPin = 0;
const int yellowLedPin = 1;
const int redLedPin = 2;

// Variable to store user input
char userInput;

void setup() {
    // Initialize LED pins as outputs
    pinMode(greenLedPin, OUTPUT);
    pinMode(yellowLedPin, OUTPUT);
    pinMode(redLedPin, OUTPUT);

    // Initialize serial communication
    Serial.begin(9600);
}

void loop() {
    // Check if serial data is available
    if (Serial.available() > 0) {
        // Read the user input
        userInput = Serial.read();

        // Process user input
        if (userInput == 'g') {
            // Turn on green LED
            digitalWrite(greenLedPin, HIGH);
            digitalWrite(yellowLedPin, LOW);
            digitalWrite(redLedPin, LOW);
        }
        else if (userInput == 'y') {
            // Turn on yellow LED
            digitalWrite(greenLedPin, LOW);
            digitalWrite(yellowLedPin, HIGH);
            digitalWrite(redLedPin, LOW);
        }
        else if (userInput == 'r') {
            // Turn on red LED
            digitalWrite(greenLedPin, LOW);
            digitalWrite(yellowLedPin, LOW);
            digitalWrite(redLedPin, HIGH);
        }
        else if (userInput == 'b') {
            // Blink green LED
            digitalWrite(yellowLedPin, LOW);
            digitalWrite(redLedPin, LOW);
            for (int i = 0; i < 5; i++) {
                digitalWrite(greenLedPin, HIGH);
                delay(500);
                digitalWrite(greenLedPin, LOW);
                delay(500);
            }
        }
    }
}
