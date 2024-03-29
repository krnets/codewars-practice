#pragma once

#include <vector>
#include <algorithm>
#include <iterator>

#include <range/v3/view/filter.hpp>
#include <range/v3/to_container.hpp>

using std::vector;


/*
std::vector<int> divisible_by(std::vector<int> numbers, int divisor)
{
	std::vector<int> ans;

	for (int num : numbers)
		if (num % divisor == 0)
			ans.push_back(num);

	return ans;
}
*/

/*
std::vector<int> divisible_by(std::vector<int> numbers, int divisor)
{
	std::vector<int> ans;

	std::copy_if(numbers.begin(), numbers.end(), std::back_inserter(ans),
	             [divisor](int x) { return x % divisor == 0; });

	return ans;
}
*/

/*
std::vector<int> divisible_by(std::vector<int> numbers, int divisor)
{
	auto it = std::remove_if(numbers.begin(),
	                         numbers.end(),
	                         [divisor](int x) { return x % divisor; });

	numbers.erase(it, numbers.end());

	return numbers;
}
*/

vector<int> divisible_by(vector<int> numbers, int divisor)
{
	return numbers
		| ranges::views::filter([&](int x) { return x % divisor == 0; })
		| ranges::to<vector<int>>();
}
