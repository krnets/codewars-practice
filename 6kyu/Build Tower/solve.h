#pragma once

using std::string;
using std::vector;

class Kata
{
public:
	vector<string> towerBuilder(int nFloors)
	{
		vector<string> tower;
		int mid = nFloors - 1;

		for (int i = 0; i < nFloors; ++i)
		{
			string floor = string(2 * nFloors - 1, ' ');

			for (int j = mid; j <= (mid + i); ++j)
			{
				floor[j] = '*';
				floor[j - i] = '*';
			}

			tower.push_back(floor);
		}

		return tower;
	}
};
