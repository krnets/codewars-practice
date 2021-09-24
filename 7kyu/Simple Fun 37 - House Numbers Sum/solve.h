#pragma once

#include <numeric>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/take_while.hpp>
#include <range/v3/algorithm/find.hpp>

/*
int house_numbers_sum(const std::vector<int>& arr)
{
	auto is_not_zero = [](int x) { return x != 0; };

	return ranges::accumulate(arr | ranges::views::take_while(is_not_zero), 0);
}
*/

int house_numbers_sum(const std::vector<int>& arr)
{
	return std::accumulate(arr.begin(), ::ranges::find(arr, 0), 0);
}
