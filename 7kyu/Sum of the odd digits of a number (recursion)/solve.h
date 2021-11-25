#pragma once

int sum_odd_digits(int n)
{
	if (n == 0) return 0;

	return sum_odd_digits(n / 10) + (n & 1 ? n % 10 : 0);
}
