#pragma once

#include <range/v3/action/sort.hpp>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/take_last.hpp>

int maxProduct(std::vector<int> numbers, int sub_size)
{
	auto rng = numbers
		| ranges::views::all
		| ranges::actions::sort
		| ranges::views::take_last(sub_size);

	return ranges::accumulate(rng, 1, std::multiplies());
}
