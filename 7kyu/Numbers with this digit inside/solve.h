#pragma once

std::vector<long> numbersWithDigitInside(long x, long d)
{
	long count = 0, sum = 0, product = 1;

	for (long i = 1; i <= x; ++i)
	{
		long n = i;

		while (n > 0)
		{
			if (n % 10 == d)
			{
				count++;
				sum += i;
				product *= i;

				break;
			}

			n /= 10;
		}
	}

	return {count, sum, (count == 0 ? 0 : product)};
}
