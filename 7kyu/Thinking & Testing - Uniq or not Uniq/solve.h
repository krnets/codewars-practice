#pragma once
#include <set>

/*
std::vector<int> testit(std::vector<int> a, std::vector<int> b)
{
	std::set<int> set_a(a.begin(), a.end());
	std::set<int> set_b(b.begin(), b.end());

	std::vector<int> v;
	v.reserve(set_a.size() + set_b.size());

	std::copy(set_a.begin(), set_a.end(), std::back_inserter(v));
	std::copy(set_b.begin(), set_b.end(), std::back_inserter(v));
	std::sort(v.begin(), v.end());

	return v;
}
*/

/*
std::vector<int> testit(std::vector<int> a, std::vector<int> b)
{
	std::set<int> set_a(a.begin(), a.end());
	std::set<int> set_b(b.begin(), b.end());

	std::vector<int> v;
	v.reserve(set_a.size() + set_b.size());

	copy(set_a.begin(), set_a.end(), std::back_inserter(v));
	copy(set_b.begin(), set_b.end(), std::back_inserter(v));
	sort(v.begin(), v.end());

	return v;
}
*/

/*
std::vector<int> testit(std::vector<int> a, std::vector<int> b)
{
	std::set<int> set_a(a.begin(), a.end());
	std::set<int> set_b(b.begin(), b.end());

	a.assign(set_a.begin(), set_a.end());
	a.reserve(set_a.size() + set_b.size());
	a.insert(a.end(), set_b.begin(), set_b.end());

	sort(a.begin(), a.end());

	return a;
}
*/


#include <range/v3/action/sort.hpp>
#include <range/v3/view/all.hpp>
#include <range/v3/view/concat.hpp>
#include <range/v3/view/unique.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;

std::vector<int> testit(std::vector<int> a, std::vector<int> b)
{
	auto rng_a = a | views::all | actions::sort | views::unique | to<std::vector<int>>();
	auto rng_b = b | views::all | actions::sort | views::unique | to<std::vector<int>>();

	return views::concat(rng_a, rng_b)
		| actions::sort
		| to<std::vector<int>>();
}
