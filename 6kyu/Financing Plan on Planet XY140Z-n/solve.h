#pragma once

/*
class Finance
{
public:
	static unsigned long long finance(unsigned long long n)
	{
		return n == 0 ? 0 : (n + 2 * n) * (n + 1) / 2 + finance(n - 1);
	}
};
*/

class Finance
{
public:
	static unsigned long long finance(unsigned long long n)
	{
		return n * (n + 1) * (n + 2) / 2;
	}
};
