#pragma once

/*
using std::vector;

bool is_eviternity_num(int n)
{
	if (n == 0) return false;

	vector<int> digits(10);
	int count_invalid = 0;

	while (n > 0)
	{
		digits[n % 10]++;
		n /= 10;
	}

	for (int i = 0; i < 10; ++i)
	{
		if (i == 3 || i == 5 || i == 8)
			continue;

		if (digits[i] > 0)
			++count_invalid;
	}
	return count_invalid == 0 &&
		digits[8] >= digits[5] && digits[5] >= digits[3];
}
*/

bool is_eviternity_num(int n)
{
	if (n == 0) return false;

	int count3s = 0, count5s = 0, count8s = 0;

	while (n > 0)
	{
		switch (n % 10)
		{
		case 3: ++count3s; break;
		case 5: ++count5s; break;
		case 8: ++count8s; break;
		default: return false;
		}
		n /= 10;
	}
	return (count3s <= count5s) && (count5s <= count8s);
}

int solve(int a, int b)
{
	int count = 0;

	for (int i = a; i < b; ++i)
		if (is_eviternity_num(i))
			++count;

	return count;
}
