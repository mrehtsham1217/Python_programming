#include <iostream>
using namespace std;

int main()
{
    const int SIZE = 100;
    const float omega = 1.8;
    // Declaring array for finding the nth values of SOR  method
    float T1[SIZE];
    float T2[SIZE];
    float T3[SIZE];
    float T4[SIZE];
    // Initializing the first values 0
    T1[0] = 0;
    T2[0] = 0;
    T3[0] = 0;
    T4[0] = 0;

    for (int i = 0; i < SIZE; i++)
    {
        T1[i + 1] = omega * (160 + T2[i] + T3[i]) / 4 + (1 - omega) * T1[i];
        T2[i + 1] = omega * (140 + T1[i + 1] + T2[i]) / 4 + (1 - omega) * T2[i];
        T3[i + 1] = omega * (60 + T1[i + 1] + T4[i]) / 4 + (1 - omega) * T3[i];
        T4[i + 1] = omega * (40 + T2[i + 1] + T3[i + 1]) / 4 + (1 - omega) * T4[i];
    }
    cout << "\n-------------Output of SOR Method------------\n";
    for (int i = 0; i < SIZE; i++)
    {
        cout << T1[i + 1] << endl;
        cout << T2[i + 1] << endl;
        cout << T3[i + 1] << endl;
        cout << T4[i + 1] << endl;
        cout << "\n------------------\n";
    }
}