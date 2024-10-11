//12. Write a program to show the temperature and shows a graph of the recent measurements

#include <dht.h>

dht DHT;
#define DHT11_PIN A1

void setup() {
	Serial.begin(9600);
	Serial.println("Humidity (%),\tTemperature (C)");
}

void loop() {
	// READ DATA
	int chk = DHT.read11(DHT11_PIN);

	// DISPLAY DATA
	Serial.print(DHT.humidity, 1);
	Serial.print("\t");
	Serial.println(DHT.temperature, 1);

	delay(1000);
}
