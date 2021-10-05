#pragma once

/*
int digital_root(int n)
{
	int sum = 0;

	while (n > 0)
	{
		sum += n % 10;
		n /= 10;
	}

	return sum < 10 ? sum : digital_root(sum);
}
*/

int sum_digits(int n)
{
	int sum = 0;

	while (n != 0)
	{
		sum += n % 10;
		n /= 10;
	}

	return sum;
};

int digital_root(int n)
{
	while (n >= 10)
	{
		n = sum_digits(n);
	}

	return n;
}

/*
int digital_root(int n)
{
	return (n - 1) % 9 + 1;
}
*/
