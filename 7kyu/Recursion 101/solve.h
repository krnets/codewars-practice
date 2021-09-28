#pragma once

std::pair<int, int> solve(int a, int b)
{
	if (a == 0 or b == 0) return std::make_pair(a, b);

	if (a >= 2 * b) return solve(a - 2 * b, b);

	if (b >= 2 * a) return solve(a, b - 2 * a);

	return std::make_pair(a, b);
}
