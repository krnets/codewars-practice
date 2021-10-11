#pragma once

using std::vector;

/*
class Kata
{
public:
	vector<int> foldArray(vector<int> array, int runs)
	{
		vector v(array);

		while (runs)
		{
			int len = v.size();
			int mid = len / 2;

			for (int i = 0; i < mid; ++i)
			{
				v[i] += v[len - i - 1];
			}
			v.resize(mid + (len & 1));
			--runs;
		}
		return v;
	}
};
*/

/*
class Kata
{
public:
	vector<int> foldArray(vector<int> array, int runs)
	{
		vector v(array);

		while (runs--)
		{
			int len = v.size(), mid = len / 2;

			for (int i = 0; i < mid; ++i)
			{
				v[i] += v[len - i - 1];
				v.pop_back();
			}
		}
		return v;
	}
};
*/

class Kata
{
public:
	std::vector<int> foldArray(std::vector<int> array, int runs)
	{
		if (runs == 0) return array;

		int len = array.size(), mid = len / 2;

		for (int i = 0; i < mid; ++i)
		{
			array[i] += array[len - i - 1];
			array.pop_back();
		}
		// return foldArray(array, --runs);
		return foldArray(array, runs - 1);
	}
};
