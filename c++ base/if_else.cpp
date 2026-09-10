#include <iostream>
#include <cstdlib>

int main() {
    system("chcp 1251 > nul");

    // int num;
    // bool is_has_car = true;

    // std::cout << "Введите число: " << std::endl;
    // std::cin >> num;
    // if (num > 3 && !is_has_car) {
    //     std::cout << "Число больше 3";
    // } else if (num < 3 || is_has_car) {
    //     std::cout << "Число меньше 3";
    // } else {
    //     std::cout << "Число равно 3";
    // }


    int num;
    std::cout << "Введите число: ";
    std::cin >> num;
    switch (num) {
        case 0:
            std::cout << "Вы ввели положительное число - 0";
            break;
        
        case 1:
            std::cout << "Вы ввели положительное число - 1";
            break;
            
        default:
            break;
    } 
    return 0;
}