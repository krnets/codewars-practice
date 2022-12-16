#pragma once

#include <string>

using namespace std;

long long factorial(int x)
{
	long long ans = 1;

	while (x > 0)
	{
		ans *= x;
		--x;
	}
	return ans;
};

string strong_num(int number)
{
	long sum = 0;

	for (char c : to_string(number))
	{
		sum += factorial(c - '0');
	}
	return sum == number ? "STRONG!!!!" : "Not Strong !!";
}
