#pragma once

#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/filter.hpp>
#include <range/v3/view/iota.hpp>

using namespace ranges;

int solution(int x)
{
	return accumulate(views::iota(1, std::max(1, x)) | views::filter([](int x) { return x % 3 == 0 || x % 5 == 0; }), 0);
}
