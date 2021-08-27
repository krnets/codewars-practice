#pragma once

/*
std::vector<int> two_oldest_ages(std::vector<int> ages)
{
	std::vector<int> v;
	std::sort(ages.begin(), ages.end());
	v.push_back(*(ages.end() - 2));
	v.push_back(*(ages.end() - 1));

	return v;
}
*/

/*
std::vector<int> two_oldest_ages(std::vector<int> ages)
{
	std::sort(ages.begin(), ages.end());

	return {*(ages.end() - 2), *(ages.end() - 1)};
}
*/

std::vector<int> two_oldest_ages(std::vector<int> ages)
{
	std::sort(ages.rbegin(), ages.rend());

	return {ages.at(1), ages.at(0)};
}
