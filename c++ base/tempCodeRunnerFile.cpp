#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;

int main() {
    system("chcp 1251 > nul");
    srand(time(NULL));

    int a, b;
    cout << "Давай сыграем в игру!" << endl;
    cout << "Тебе надо будет угадать рандомное число" << endl;
    cout << "Задай границы рандомного числа (минимум -10К, максимум - 10К)" << endl;
    cout << "Задай минимальное число (например: -2400): ";
    cin >> a;
    cout << "Задай максимальное число (например: 8200): ";
    cin >> b;
    cout << "Отлично границы рандомного числа заданы" << endl;
    cout << "Начинаем игру" << endl;
    
    bool stop = false;
    int count_xod = 0;
    int rand_num = a + rand() % (b - a + 1);
    int user_input;
    do {
        cout << "Введи число: ";
        cin >> user_input;
        count_xod += 1;
        if (user_input == rand_num) {
            stop = true;
        } else {
            if (user_input < rand_num) {
                cout << "К сожалению мимо(" << endl;
                cout << "Подсказка: попробуй взять число больше" << endl;
            } else {
                cout << "К сожалению мимо(" << endl;
                cout << "Подсказка: попробуй взять число меньше" << endl;
            }
        }
    } while (!stop);
    cout << "Вы выиграли!!!" << endl;
    cout << "Вам потребовалось " << count_xod << " ходов" << endl;  


    return 0;
}