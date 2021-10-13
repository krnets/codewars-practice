#pragma once

#include <range/v3/algorithm/any_of.hpp>
#include <range/v3/algorithm/count_if.hpp>

using namespace ranges;
using std::string;

/*
string bingo(std::vector<std::pair<string, int>> ticket, int win)
{
	int count = 0;

	for (std::pair<string, int>& p : ticket)
		for (char& c : p.first)
			if (c == p.second)
			{
				++count;
				break;
			}

	return count >= win ? "Winner!" : "Loser!";
}
*/

string bingo(std::vector<std::pair<string, int>> ticket, int win)
{
	auto pred = [](auto& p)
	{
		return any_of(p.first, [&p](char& c) { return c == p.second; });
	};
	return count_if(ticket, pred) < win ? "Loser!" : "Winner!";
}
