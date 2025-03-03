#include <conio.h>
#include <iostream>
#include <graphics.h>
#include <stdlib.h>
#include <math.h>

class Point {
public:
    int x, y;

    Point() : x(0), y(0) {}

    Point(int x, int y) : x(x), y(y) {}

    Point operator+(const Point& other) const {
        return Point(x + other.x, y + other.y);
    }

    Point operator*(float scalar) const {
        return Point(static_cast<int>(x * scalar), static_cast<int>(y * scalar));
    }

    Point rotate(float angle) const {
        float radian = angle * 3.14159 / 180.0;
        return Point(static_cast<int>(x * cos(radian) - y * sin(radian)),
            static_cast<int>(x * sin(radian) + y * cos(radian)));
    }

    void draw() const {
        putpixel(x, y, WHITE);
    }
};

class Object {
protected:
    Point position;

public:
    Object(int x, int y) : position(x, y) {}

    virtual void draw() const = 0;

    void scale(float factor) {
        position = position * factor;
    }

    void translate(int deltaX, int deltaY) {
        position = position + Point(deltaX, deltaY);
    }

    void rotate(float angle) {
        position = position.rotate(angle);
    }
};

class Square : public Object {
public:
    Square(int x, int y) : Object(x, y) {}

    void draw() const override {
        rectangle(position.x - 10, position.y - 10, position.x + 10, position.y + 10);
    }
};

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TC\\BGI");

    Square square(100, 100);

    char choice;
    do {
        cleardevice();

        std::cout << "Choose Transformation:\n";
        std::cout << "1. Scale\n";
        std::cout << "2. Translate\n";
        std::cout << "3. Rotate\n";

        int option;
        std::cout << "Enter your choice (1-3): ";
        std::cin >> option;

        switch (option) {
        case 1:
            float scale_factor;
            std::cout << "Enter scale factor: ";
            std::cin >> scale_factor;
            square.scale(scale_factor);
            break;
        case 2:
            int delta_x, delta_y;
            std::cout << "Enter translation (delta_x delta_y): ";
            std::cin >> delta_x >> delta_y;
            square.translate(delta_x, delta_y);
            break;
        case 3:
            float angle;
            std::cout << "Enter rotation angle (in degrees): ";
            std::cin >> angle;
            square.rotate(angle);
            break;
        default:
            std::cout << "Invalid choice!\n";
            break;
        }

        square.draw();
        delay(1000);

        std::cout << "Do you want to continue? (y/n): ";
        std::cin >> choice;

    } while (choice == 'y' || choice == 'Y');

    closegraph();

    return 0;
}
