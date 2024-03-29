#include <wiringPi.h>
#include <iostream>
#include <string>

void setRed();
void setGreen();
void flashRed();
void setupPins();

using namespace std;

int main(int argc, char* argv[]) {
    setupPins();

    if (argc == 2) {
        string in(argv[1]);

        if (in == "red") {
            setRed();
        }
        else if (in == "green") {
            setGreen();
        }
        else {
            flashRed();  // flash for an error in default case
        }
        return 0;
    }
    else {
        return 1;
    }
    
}

void setRed() {
    digitalWrite(0, 1);
}

void setGreen() {
    digitalWrite(1, 1);
}

void flashRed() {
    digitalWrite(2, 1);
}

void setupPins() {
    wiringPiSetup();
    pinMode(0, OUTPUT);
    pinMode(1, OUTPUT);
    pinMode(2, OUTPUT);
    digitalWrite(0, 0);
    digitalWrite(1, 0);
    digitalWrite(2, 0);
}

