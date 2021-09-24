#pragma once

std::string cake(int x, std::string y)
{
	int sum = 0;

	for (size_t i = 0; i < y.length(); ++i)
	{
		if (i % 2 == 0)
			sum += y[i];
		else
			sum += y[i] - 'a' + 1;
	}

	return sum < (x * 0.7) ? "That was close!" : "Fire!";
}
