#pragma once

// F(0) = 1
// M(0) = 0
// F(n) = n - M(F(n - 1))
// M(n) = n - F(M(n - 1))


int M(int n);

int F(int n)
{
	if (n == 0) return 1;

	return n - M(F(n - 1));
}

int M(int n)
{
	if (n == 0) return 0;

	return n - F(M(n - 1));
}
