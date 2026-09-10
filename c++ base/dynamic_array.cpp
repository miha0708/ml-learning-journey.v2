#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    system("chcp 1251 > nul");

    int *nums = new int[300000000000];
    nums[0] = 30;
    cout << nums[0];    
    delete[] nums;

    return 0;
}