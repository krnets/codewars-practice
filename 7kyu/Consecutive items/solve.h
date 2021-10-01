#pragma once

/*
You are given a list of unique integers arr, and two integers a and b.
Your task is to find out whether or not a and b appear consecutively in arr.

It is guaranteed that a and b are both present in arr.
*/

bool consecutive(std::vector<int> arr, int a, int b)
{
	int x = 0, y = 0;

	for (int i = 0; i < arr.size(); ++i)
	{
		if (arr[i] == a) x = i;
		if (arr[i] == b) y = i;
	}

	return abs(x - y) == 1;
}
