#pragma once

/*
long long mygcd(long long a, long long b)
{
	return b == 0 ? a : mygcd(b, a % b);
}
*/

long long mygcd(long long a, long long b)
{
	long long tmp;

	while (b != 0)
	{
		tmp = a;
		a = b;
		b = tmp % b;
	}

	return a;
}
