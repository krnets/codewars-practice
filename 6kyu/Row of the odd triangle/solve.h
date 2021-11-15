#pragma once

using ULL = unsigned long long;


std::vector<ULL> odd_row(unsigned int n)
{
	std::vector<ULL> v(n);
	ULL m = n - 1;
	m = m * n + 1;

	for (ULL i = 0; i < n; ++i)
		v[i] = m + 2 * i;

	return v;
}
