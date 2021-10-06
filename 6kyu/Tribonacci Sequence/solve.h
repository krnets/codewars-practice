#pragma once

using std::vector;

/*
vector<int> tribonacci(vector<int> signature, int n)
{
	if (n == 0) return vector<int>();

	vector<int> result(n);

	std::copy(signature.begin(), signature.end(), result.begin());

	for (int i = 3; i < n; ++i)
	{
		result[i] = result[i - 1] + result[i - 2] + result[i - 3];
	}

	return result;
}
*/

vector<int> tribonacci(vector<int> signature, int n)
{
	signature.resize(n);

	for (int i = 3; i < n; ++i)
	{
		signature[i] = signature[i - 1] + signature[i - 2] + signature[i - 3];
	}

	return signature;
}
