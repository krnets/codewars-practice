#pragma once

using std::vector;

/*
vector<vector<int>> matrixAddition(vector<vector<int>> a, vector<vector<int>> b)
{
	for (int i = 0; i < a.size(); ++i)
		for (int j = 0; j < b.size(); ++j)
			a[i][j] += b[i][j];

	return a;
}
*/

/*
vector<vector<int>> matrixAddition(vector<vector<int>> a, vector<vector<int>> b)
{
	auto ita = a.begin();
	auto itb = b.begin();

	while (ita != a.end())
	{
		std::transform(ita->begin(), ita->end(), itb->begin(), ita->begin(), std::plus());
		++ita, ++itb;
	}

	return a;
}
*/

using matrix = std::vector<std::vector<int>>;

matrix matrixAddition(matrix a, matrix b)
{
	auto it = a.begin(), xt = b.begin();

	while (it != a.end())
	{
		std::transform(it->begin(), it->end(), xt->begin(), it->begin(), std::plus());
		++it, ++xt;
	}

	return a;
}
