//11. Write a program so it displays the temperature in Fahrenheit as well as the maximum and minimum temperatures it has seen

#include <dht.h>

dht DHT;
#define DHT11_PIN A1

float min_t, max_t;

void setup() {
    Serial.begin(9600);
    Serial.println("Humidity (%),\tTemperature (C),\tTemperature (F),\tMin Temp (C),\tMax Temp (C)");
    min_t = 1000; // Initializing min_t to a high value
    max_t = -1000; // Initializing max_t to a low value
}

void loop() {
    // READ DATA
    int chk = DHT.read11(DHT11_PIN);

    // Update min and max temperatures
    if (DHT.temperature < min_t) {
        min_t = DHT.temperature;
    }
    if (DHT.temperature > max_t) {
        max_t = DHT.temperature;
    }

    // DISPLAY DATA
    Serial.print(DHT.humidity, 1);
    Serial.print("%\t");
    Serial.print(DHT.temperature, 1);
    Serial.print("C\t");
    Serial.print((DHT.temperature * 1.8) + 32, 1);
    Serial.print("F\t");
    Serial.print(min_t, 1);
    Serial.print("C\t");
    Serial.print(max_t, 1);
    Serial.println("C");

    delay(1000);
}

