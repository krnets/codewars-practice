#pragma once

int findDigit(int num, int nth)
{
	if (nth <= 0) return -1;

	int ret = 0;

	while (nth > 0)
	{
		ret = num % 10;
		num /= 10;
		nth--;
	}

	return std::abs(ret);
}
