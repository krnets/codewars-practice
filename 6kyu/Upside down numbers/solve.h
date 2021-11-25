#pragma once

bool is_upside_down(int n)
{
	if (n == 0 || n == 1 || n == 8) return true;

	int x = n;
	int z = 0;
	std::set set{2, 3, 4, 5, 7};

	while (x > 0)
	{
		int y = x % 10;

		if (set.count(y))
			return false;

		y = (y == 9) ? 6 : (y == 6) ? 9 : y;
		z = 10 * z + y;
		x /= 10;
	}
	return z == n;
}

int solve(int x, int y)
{
	int count = 0;

	for (int i = x; i < y; ++i)
		if (is_upside_down(i))
			++count;

	return count;
}
