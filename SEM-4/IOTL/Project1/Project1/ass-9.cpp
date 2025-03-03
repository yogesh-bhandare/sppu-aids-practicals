//9. Write a program to control the color of the LED by turning 3 different potentiometers.One will be read for the value of Red, one for the value of Green, and one for the value of Blue

int red_light_pin = 5;
int green_light_pin = 6;
int blue_light_pin = 3;
unsigned int red, green, blue;

void setup() {
	pinMode(red_light_pin, OUTPUT);
	pinMode(green_light_pin, OUTPUT);
	pinMode(blue_light_pin, OUTPUT);
}

void loop() {
	red = analogRead(A0);
	red = (red / 4);
	green = analogRead(A2);
	green = (green / 4);
	blue = analogRead(A3);
	blue = (blue / 4);

	RGB_color(255 - red, 255 - green, 255 - blue);

	delay(1000);
}

void RGB_color(int red_light_value, int green_light_value, int blue_light_value) {
	analogWrite(red_light_pin, red_light_value);
	analogWrite(green_light_pin, green_light_value);
	analogWrite(blue_light_pin, blue_light_value);
}
