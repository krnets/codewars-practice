#pragma once

using opt_int_t = std::optional<int>;
using matrix_t = std::vector<std::vector<int>>;

opt_int_t center(const matrix_t& mat)
{
	opt_int_t ans;

	int m, n = mat.size();

	if ((n & 1) && (m = mat.front().size()) & 1)
		ans.emplace(mat[n / 2][m / 2]);

	return ans;
}
