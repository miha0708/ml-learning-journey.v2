// #include <iostream>
// #include <cstdlib> // Нужно для функции system

// int main() {
//     // Принудительно ставим кодировку 1251 для консоли
//     system("chcp 1251 > nul");

//     float a, b;
//     char op;

//     std::cout << "Введите первое число: ";
//     std::cin >> a;

//     std::cout << "Введите второе число: ";
//     std::cin >> b;

//     std::cout << "Введите знак операции: ";
//     std::cin >> op;

//     if (b == 0 and op == '/') {
//         std::cout << "Нельзя делить на 0!";
//         return 0;
//     }
//     if (op == '+') {
//         std::cout << "Ответ: " << a + b;
//     } if (op == '-') {
//         std::cout << "Ответ: " << a - b;
//     } if (op == '*') {
//         std::cout << "Ответ: " << a * b;
//     } if (op == '/') {
//         std::cout << "Ответ: " << a / b;
//     } 

//     return 0;
// }