// Yogesh Bhandare S.E. AI-DS 22506
//5. Write a program using Arduino to control LED(One or more ON / OFF).Or Blinking

// Pin connected to the LED
const int ledPin = 13;

// Initialize the LED pin as an output
void setup() {
	pinMode(ledPin, OUTPUT);
}

// Main program loop
void loop() {
	// Turn on the LED
	digitalWrite(ledPin, HIGH);
	delay(1000); // Wait for 1 second

	// Turn off the LED
	digitalWrite(ledPin, LOW);
	delay(1000); // Wait for 1 second
}
