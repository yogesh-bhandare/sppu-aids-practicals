//14. Understanding the connectivity of Raspberry - Pi / Beagle board circuit / Arduino with IR sensor. Write an application to detect obstacle and notify user using LEDs

void setup() {
    pinMode(4, OUTPUT); // LED pin
    pinMode(9, INPUT); // Sensor pin
}

void loop() {
    // Read the sensor state
    int sensorState = digitalRead(9);

    // Check if obstacle is detected
    if (sensorState == HIGH) {
        digitalWrite(4, HIGH); // Turn on LED
    }
    else {
        digitalWrite(4, LOW); // Turn off LED
    }
}
