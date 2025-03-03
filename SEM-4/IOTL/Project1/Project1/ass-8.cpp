void setup() {
	Serial.begin(9600);
	Serial.println("Input the number:");
}

void loop() {
	int input = Serial.parseInt();
	int inputSquared = sq(input);
	Serial.println(inputSquared);
	delay(500);
}
