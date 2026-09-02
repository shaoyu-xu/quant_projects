#include<iostream>
int main()
{
    int sum = 50;
    for (int val = 51; val <= 100; ++val)
        sum += val;
    std::cout << "Sum of 50 to 100 inclusive is "
              << sum << std::endl;
    return 0;
}