#pragma once

/*
#include <fmt/chrono.h>
#include <range/v3/algorithm.hpp>
#include <range/v3/numeric.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/view/split.hpp>
#include <range/v3/view/transform.hpp>

using namespace ranges;
using std::string;
using std::vector;

class Stat
{
public:
	static string stat(const string& strg)
	{
		auto to_seconds = [&](auto&& t)
		{
			vector<string> splits = t | views::split('|') | to<vector<string>>();
			vector<int> time = splits | views::transform([](auto&& s) { return std::stoi(s); }) | to<vector<int>>();

			return time[0] * 60 * 60 + time[1] * 60 + time[2];
		};
		vector<int> player_times = strg | views::split(' ') | views::transform(to_seconds) | to<vector<int>>();
		sort(player_times);

		int n = player_times.size();
		int rng = *max_element(player_times) - *min_element(player_times);
		int avg = accumulate(player_times, 0) / n;
		int med = n & 1 ? player_times[n / 2] : (player_times[n / 2 - 1] + player_times[n / 2]) / 2;

		auto t_rng = tm(), t_avg = tm(), t_med = tm();
		t_rng.tm_hour = rng / 60 / 60, t_rng.tm_min = rng / 60 % 60, t_rng.tm_sec = rng % 60;
		t_avg.tm_hour = avg / 60 / 60, t_avg.tm_min = avg / 60 % 60, t_avg.tm_sec = avg % 60;
		t_med.tm_hour = med / 60 / 60, t_med.tm_min = med / 60 % 60, t_med.tm_sec = med % 60;

		string s = "Range: {:%H|%M|%S} Average: {:%H|%M|%S} Median: {:%H|%M|%S}";

		return fmt::format(s, t_rng, t_avg, t_med);
	}
};
*/


#include <regex>
#include <fmt/chrono.h>
#include <range/v3/algorithm/sort.hpp>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/tokenize.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;
using std::vector;

class Stat
{
public:
	static string stat(const string& strg)
	{
		auto to_seconds = [](auto&& token)
		{
			vector<int> time = token | views::tokenize(std::regex{"[^|]+"})
				| views::transform([](auto&& s) { return std::stoi(s); }) | to<vector<int>>();

			return time[0] * 3600 + time[1] * 60 + time[2];
		};
		auto players = strg | views::tokenize(std::regex{"\\S+"}) | to<vector<string>>();
		auto player_times = players | views::transform(to_seconds) | to<vector<int>>();
		sort(player_times);

		int n = player_times.size();
		int rng = player_times.back() - player_times.front();
		int avg = accumulate(player_times, 0) / n;
		int med = n & 1 ? player_times[n / 2] : (player_times[n / 2 - 1] + player_times[n / 2]) / 2;

		tm t_rng = tm(), t_avg = tm(), t_med = tm();
		t_rng.tm_hour = rng / 3600, t_rng.tm_min = rng / 60 % 60, t_rng.tm_sec = rng % 60;
		t_avg.tm_hour = avg / 3600, t_avg.tm_min = avg / 60 % 60, t_avg.tm_sec = avg % 60;
		t_med.tm_hour = med / 3600, t_med.tm_min = med / 60 % 60, t_med.tm_sec = med % 60;

		string s = "Range: {:%H|%M|%S} Average: {:%H|%M|%S} Median: {:%H|%M|%S}";

		return fmt::format(s, t_rng, t_avg, t_med);
	}
};
