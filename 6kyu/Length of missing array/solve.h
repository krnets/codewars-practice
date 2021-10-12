#pragma once

using std::vector;

template <class TYPE>
int getLengthOfMissingArray(vector<vector<TYPE>> arrayOfArrays)
{
	if (arrayOfArrays.size() == 0) return 0;

	vector<int> lengths;
	int sum = 0, min = INT32_MAX, max = 0;

	for (vector<TYPE> array : arrayOfArrays)
	{
		int size = array.size();

		if (size == 0) return 0;

		if (size < min)
			min = size;
		else if (size > max)
			max = size;

		sum += size;
	}

	int expected_sum = (max - min + 1) * (min + max) / 2;

	return expected_sum - sum;
}
