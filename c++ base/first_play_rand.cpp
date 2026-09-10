#include <iostream>
#include <cstdlib>
#include <time.h>
#include <windows.h>
using namespace std;

int main() {
    system("chcp 1251 > nul");
    srand(time(NULL));

    int a, b;
    cout << "Давай сыграем в игру!" << endl;
    Sleep(1000);
    cout << "Тебе надо будет угадать рандомное число" << endl;
    Sleep(1000);
    cout << "Задай границы рандомного числа (минимум -10К, максимум - 10К)" << endl;
    Sleep(1000);
    cout << "Задай минимальное число (например: -2400): ";
    Sleep(1000);
    cin >> a;
    cout << "Задай максимальное число (например: 8200): ";
    Sleep(1000);
    cin >> b;
    cout << "Отлично границы рандомного числа заданы" << endl;
    Sleep(1000);
    cout << "Начинаем игру" << endl;
    Sleep(1000);
    
    bool stop = false;
    int count_xod = 0;
    int rand_num = a + rand() % (b - a + 1);
    int user_input;
    do {
        Sleep(300);
        cout << "Введи число: ";
        cin >> user_input;
        count_xod += 1;
        if (user_input == rand_num) {
            stop = true;
        } else {
            if (user_input < rand_num) {
                cout << "К сожалению мимо(" << endl;
                Sleep(100);
                cout << "Подсказка: попробуй взять число больше" << endl;
                Sleep(100);
            } else {
                cout << "К сожалению мимо(" << endl;
                Sleep(100);
                cout << "Подсказка: попробуй взять число меньше" << endl;
                Sleep(100);
            }
        }
    } while (!stop);
    cout << "Вы выиграли!!!" << endl;
    Sleep(100);
    cout << "Вам потребовалось " << count_xod << " ходов" << endl;  


    return 0;
}