#include <unordered_map>

std::string rps(const std::string& p1, const std::string& p2)
{
	std::unordered_map<std::string, std::string> map{
		{"scissors", "paper"},
		{"paper", "rock"},
		{"rock", "scissors"}
	};

	return p1 == p2 ? "Draw!" : map[p1] == p2 ? "Player 1 won!" : "Player 2 won!";
}
