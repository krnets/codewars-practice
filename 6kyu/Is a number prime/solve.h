#pragma once

bool isPrime(int num)
{
	if (num <= 1) return false;
	if (num <= 3 || num == 5) return true;
	if (num % 2 == 0 || num % 3 == 0 || num % 5 == 0) return false;

	int limit = sqrt(num);

	for (int i = 5; i <= limit; i += 6)
		if (num % i == 0 || num % (i + 2) == 0)
			return false;

	return true;
}
