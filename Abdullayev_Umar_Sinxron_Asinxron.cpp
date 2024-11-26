#include <iostream>
#include <thread>
#include <chrono>

using namespace std;

// Sinxron va Asinxron uchun ikkita funksiya
void vazifa1() {
    cout << "Vazifa 1: Choy qaynatilmoqda..." << endl;
    this_thread::sleep_for(chrono::seconds(3)); // 3 soniya kutish
    cout << "Vazifa 1: Choy tayyor!" << endl;
}

void vazifa2() {
    cout << "Vazifa 2: Pechenye qo'yilmoqda..." << endl;
    this_thread::sleep_for(chrono::seconds(2)); // 2 soniya kutish
    cout << "Vazifa 2: Pechenye tayyor!" << endl;
}

int main() {
    // Sinxron jarayon
    cout << "Sinxron jarayon boshlanmoqda...\n" << endl;
    vazifa1(); // Choy qaynatish
    vazifa2(); // Pechenye qo‘yish
    cout << "\nSinxron jarayon tugadi.\n" << endl;

    // Asinxron jarayon
    cout << "Asinxron jarayon boshlanmoqda...\n" << endl;
    thread t1(vazifa1); // Choy qaynatishni alohida oqimda bajarish
    thread t2(vazifa2); // Pechenye qo‘yishni alohida oqimda bajarish

    t1.join(); // Vazifa 1 tugashini kutish
    t2.join(); // Vazifa 2 tugashini kutish
    cout << "\nAsinxron jarayon tugadi." << endl;

    return 0;
}
