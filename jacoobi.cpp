#include <iostream>
using namespace std;

int main()
{
    const int SIZE = 10;
    // Declaring array for finding the nth values of Gause Sidel method
    float T1[SIZE];
    float T2[SIZE];
    float T3[SIZE];
    float T4[SIZE];
    // Initializing the first values 0
    T1[0] = 0;
    T2[0] = 0;
    T3[0] = 0;
    T4[0] = 0;

    // Equation of Gause Sidel method
    for (int i = 0; i < SIZE; i++)
    {
        T1[i + 1] = (160 + T2[i] + T3[i]) / 4;
        T2[i + 1] = (140 + T1[i] + T2[i]) / 4;
        T3[i + 1] = (60 + T1[i] + T4[i]) / 4;
        T4[i + 1] = (40 + T2[i] + T3[i]) / 4;
    }

    for (int i = 0; i < SIZE; i++)
    {
        cout << T1[i + 1] << "\n";
        cout << T2[i + 1] << "\n";
        cout << T3[i + 1] << "\n";
        cout << T4[i + 1] << "\n";
        cout << "\n----------------------\n";
    }

    return 0;
}