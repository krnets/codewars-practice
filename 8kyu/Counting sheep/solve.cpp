/*
#include <vector>

int count_sheep(std::vector<bool> arr)
{
	int counted = 0;

	for (bool x : arr)
		if (x)
			counted++;

	return counted;
}
*/


#include <vector>

int count_sheep(std::vector<bool> arr)
{
	return std::count(arr.begin(), arr.end(), true);
}
