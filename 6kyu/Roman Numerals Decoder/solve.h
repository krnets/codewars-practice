#pragma once

/*
int solution(std::string roman)
{
	std::map<char, int> map{
		{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
		{'C', 100}, {'D', 500}, {'M', 1000}
	};

	int ans = 0;

	for (size_t i = 0; i < roman.length(); ++i)
	{
		int current = map[roman[i]];

		if (i < roman.length() - 1 && current < map[roman[i + 1]])
			ans -= current;
		else
			ans += current;
	}

	return ans;
}
*/

std::map<char, int> rtoi_map{{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};

int solution(std::string roman)
{
	int ans = 0;

	for (size_t i = 1; i < roman.length(); ++i)
	{
		int curr = rtoi_map[roman[i - 1]];
		int next = rtoi_map[roman[i]];
		ans += (curr < next) ? -curr : curr;
	}

	return ans + rtoi_map[roman.back()];
}
