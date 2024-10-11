//6. Create a program that illuminates the green LED if the counter is less than 100, illuminates the yellow LED if the counter is between 101 and 200 and illuminates the red LED if the counter is greater than 200

// Pins connected to the LEDs
const int greenLedPin = 0;
const int yellowLedPin = 1;
const int redLedPin = 2;

// Counter variable
int counter = 0;

void setup() {
    // Initialize LED pins as outputs
    pinMode(greenLedPin, OUTPUT);
    pinMode(yellowLedPin, OUTPUT);
    pinMode(redLedPin, OUTPUT);
}

void loop() {
    // Increment the counter
    counter++;

    // Check the counter value and control LEDs accordingly
    if (counter < 100) {
        // Turn on green LED
        digitalWrite(greenLedPin, HIGH);
        digitalWrite(yellowLedPin, LOW);
        digitalWrite(redLedPin, LOW);
    }
    else if (counter >= 100 && counter <= 200) {
        // Turn on yellow LED
        digitalWrite(greenLedPin, LOW);
        digitalWrite(yellowLedPin, HIGH);
        digitalWrite(redLedPin, LOW);
    }
    else {
        // Turn on red LED
        digitalWrite(greenLedPin, LOW);
        digitalWrite(yellowLedPin, LOW);
        digitalWrite(redLedPin, HIGH);
    }

    // Reset counter if it exceeds 300
    if (counter > 300) {
        counter = 0;
    }

    // Delay for some time
    delay(100);
}
