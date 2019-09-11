#include <iostream>
#include <string>

void setRed();
void setGreen();
void flashRed();

using namespace std;

int main(int argc, char* argv[]) {

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
    cout << "red" << endl;
}

void setGreen() {
    cout << "green" << endl;
}

void flashRed() {
    cout << "flashing red" << endl;
}