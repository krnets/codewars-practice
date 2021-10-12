#pragma once

using std::vector;

/*
vector<int> beggars(const vector<int>& values, unsigned int n)
{
	vector<int> amounts(n);

	if (n == 0) return amounts;

	for (int i = 0; i < values.size(); ++i)
	{
		amounts[i % n] += values[i];
	}

	return amounts;
}
*/

/*
vector<int> beggars(const vector<int>& values, unsigned int n)
{
	vector<int> amounts(n);

	if (n)
	{
		for (int i = 0; i < values.size(); ++i)
		{
			amounts[i % n] += values[i];
		}
	}

	return amounts;
}
*/


vector<int> beggars(const vector<int>& values, unsigned int n, int pos, vector<int>& amounts)
{
	if (pos == values.size()) return amounts;

	amounts[pos % n] += values[pos];

	return beggars(values, n, pos + 1, amounts);
}

vector<int> beggars(const vector<int>& values, unsigned int n)
{
	vector<int> amounts(n);

	return n == 0 ? amounts : beggars(values, n, 0, amounts);
}
