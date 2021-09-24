#pragma once

unsigned int squaresNeeded(long long n)
{
	return ceil(log2(n + 1));
}

