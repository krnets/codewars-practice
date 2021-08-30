#pragma once

/*
long long factorial(int n)
{
	return n == 0 ? 1 : n * factorial(n - 1);
}
*/

long long factorial(int n)
{
	long long ans = 1;

	while (n > 1)
	{
		ans *= n;
		--n;
	}

	return ans;
}
