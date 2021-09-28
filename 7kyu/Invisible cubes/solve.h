#pragma once

unsigned long long notVisibleCubes(unsigned int n)
{
	return n <= 1 ? 0 : (n - 2ull) * (n - 2) * (n - 2);
}
