#include <vector>

std::vector<int> humanYearsCatYearsDogYears(int humanYears)
{
	std::vector<int> vec;
	vec.reserve(3);
	vec.push_back(humanYears);

	int catYears = 0;
	int dogYears = 0;

	if (humanYears > 0)
	{
		catYears += 15;
		dogYears += 15;
	}
	if (humanYears > 1)
	{
		catYears += 9;
		dogYears += 9;
	}
	if (humanYears > 2)
	{
		catYears += 4 * (humanYears - 2);
		dogYears += 5 * (humanYears - 2);
	}

	vec.push_back(catYears);
	vec.push_back(dogYears);

	return vec;
}
