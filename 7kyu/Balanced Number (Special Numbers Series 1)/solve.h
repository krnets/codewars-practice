#pragma once
#include <string>
using namespace std;

/*
int sum_digits(int n)
{
	int sum = 0;

	while (n > 0)
	{
		sum += n % 10;
		n /= 10;
	}
	return sum;
};

string balancedNum(unsigned long long int number)
{
	string n_string = to_string(number);
	int length = n_string.length();

	if (length <= 2)
		return "Balanced";

	string left = n_string.substr(0, (length + 1) / 2 - 1);
	string right = n_string.substr(length / 2 + 1);

	int sum_left = sum_digits(stoi(left));
	int sum_right = sum_digits(stoi(right));

	return sum_left == sum_right ? "Balanced" : "Not Balanced";
}
*/

string balancedNum(unsigned long long int number)
{
	int balance = 0;
	string n_str = to_string(number);
	int length = n_str.length();
	int mid = length / 2 + 1;

	for (int i = 0, j = mid; j < length; ++i, ++j)
	{
		balance += n_str[i];
		balance -= n_str[j];
	}

	return balance == 0 ? "Balanced" : "Not Balanced";
}
