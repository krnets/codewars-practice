#include <array>
#include <string>
#include <numeric>

/*
int points(const std::array<std::string, 10>& games)
{
	int total = 0;

	for (int i = 0; i < games.size(); ++i)
	{
		auto score = games[i];
		int pos = score.find(':');

		int x = stoi(score.substr(0, pos));
		int y = stoi(score.substr(pos + 1));

		total += (x > y) ? 3 : (x == y) ? 1 : 0;
	}

	return total;
}
*/


/*
int points(const std::array<std::string, 10>& games)
{
	int total = 0;

	for (auto score : games)
	{
		int pos = score.find(':');

		int x = stoi(score.substr(0, pos));
		int y = stoi(score.substr(pos + 1));

		total += (x > y) ? 3 : (x == y) ? 1 : 0;
	}

	return total;
}
*/

int points(const std::array<std::string, 10>& games)
{
	return std::accumulate(games.begin(), games.end(), 0,
	                       [](auto r, auto s)
	                       {
		                       if (s[0] == s[2]) return r + 1;
		                       if (s[0] > s[2]) return r + 3;
		                       return r;
	                       });
}
