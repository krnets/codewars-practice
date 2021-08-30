#pragma once

/*
long long over_the_road(long long address, long long n)
{
	return 2 * n - address + 1;
}
*/

long long over_the_road(long long address, long long n)
{
	return (n - address) + n + 1;
}
