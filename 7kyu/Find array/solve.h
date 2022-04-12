#pragma once
using std::vector;

template <typename T>
vector<T> find_array(vector<T> arr1, vector<int> arr2)
{
	vector<T> v;

	for (int x : arr2)
		if (x < arr1.size())
			v.push_back(arr1[x]);

	return v;
}
