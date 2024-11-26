#include <iostream>  // Konsolga chiqarish uchun
#include <thread>    // Iplar bilan ishlash uchun
#include <chrono>    // Vaqtni kutish uchun
#include <future>    // Asinxronlik uchun

using namespace std; // std kutubxonasini global darajada ishlatish

// Foydalanuvchi hisobini tekshirish vazifasi
bool tekshirUserHisobi() {
    this_thread::sleep_for(chrono::seconds(2)); // 2 soniya kutish
    cout << "Foydalanuvchi hisobini tekshirish tugadi!" << endl;
    return true; // Hisob tekshirish muvaffaqiyatli
}

// Internetdan ma'lumot olish (simulyatsiya)
string ma'lumotOlish() {
    this_thread::sleep_for(chrono::seconds(3)); // 3 soniya kutish
    cout << "Internetdan ma'lumot olish tugadi!" << endl;
    return "Ma'lumot: Asinxron operatsiya";
}

// Hisob-kitobni amalga oshirish
double hisobKitob() {
    this_thread::sleep_for(chrono::seconds(1)); // 1 soniya kutish
    cout << "Hisob-kitob yakunlandi!" << endl;
    return 45.67; // Hisob-kitob natijasi
}

int main() {
    // Asinxron vazifalarni yaratish
    future<bool> userHisobi = async(launch::async, tekshirUserHisobi);
    future<string> internetMa'lumot = async(launch::async, ma'lumotOlish);
    future<double> hisobNatija = async(launch::async, hisobKitob);

    // Boshqa operatsiyalarni shu vaqtning o'zida bajarish mumkin
    cout << "Boshqa operatsiyalarni bajarish..." << endl;

    // Asinxron vazifalar yakunlanishini kutish
    bool userVerified = userHisobi.get();       // Hisobni tekshirish natijasi
    string internetData = internetMa'lumot.get(); // Internetdan olingan ma'lumot
    double calculationResult = hisobNatija.get(); // Hisob-kitob natijasi

    // Yakuniy natijalarni chiqarish
    cout << "Hisob tekshirildi: " << (userVerified ? "Muvaffaqiyatli" : "Xato") << endl;
    cout << "Internetdan olingan ma'lumot: " << internetData << endl;
    cout << "Hisob-kitob natijasi: " << calculationResult << endl;

    cout << "Barcha asinxron vazifalar yakunlandi!" << endl;

    return 0;
}
