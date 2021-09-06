#pragma once

/*
long long int maxNumber(long long int number)
{
	std::string n_str = std::to_string(number);
	std::sort(n_str.rbegin(), n_str.rend());
	long long ans = 0;

	for (int i = 0; i < n_str.length(); ++i)
	{
		ans = 10 * ans + n_str[i] - '0';
	}

	return ans;
}
*/

/*
long long int maxNumber(long long int number)
{
	std::string n_str = std::to_string(number);
	std::sort(n_str.rbegin(), n_str.rend());

	return std::stoll(n_str);
}
*/

long long maxNumber(long long n)
{
	int arr[10] = {0};
	int pos = 10;

	while (n > 0)
	{
		arr[n % 10] += 1;
		n /= 10;
	}

	while (pos--)
	{
		int i = arr[pos];

		while (i > 0)
		{
			n = 10 * n + pos;
			i--;
		}
	}

	return n;
}
