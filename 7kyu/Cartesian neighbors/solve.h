#pragma once

using std::vector;

/*
vector<vector<int>> cartesianNeighbor(int x, int y)
{
	vector<vector<int>> vec{
		{x - 1, y - 1}, {x - 1, y}, {x - 1, y + 1},
		{x, y - 1}, {x, y + 1},
		{x + 1, y - 1}, {x + 1, y}, {x + 1, y + 1}
	};
	return vec;
}
*/

vector<vector<int>> cartesianNeighbor(int x, int y)
{
	vector<vector<int>> vec{
		{--x, y - 1}, {x, y}, {x, y + 1},
		{++x, y - 1}, {x, y + 1},
		{++x, y - 1}, {x, y}, {x, y + 1}
	};
	return vec;
}
