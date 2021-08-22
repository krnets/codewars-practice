#include <string>
#include <unordered_map>
#include <algorithm>

/*
std::string correct(std::string str)
{
	std::unordered_map<char, char> umap{{'1', 'I'}, {'0', 'O'}, {'5', 'S'}};

	std::transform(str.begin(), str.end(), str.begin(), [umap](char c)
	{
		return (umap.find(c) == umap.end() ? c : umap.at(c));
	});

	return str;
}
*/

std::string correct(std::string str)
{
	std::unordered_map<char, char> umap{{'1', 'I'}, {'0', 'O'}, {'5', 'S'}};
	char r;
	std::replace_if(str.begin(), str.end(), [&](char c) { return r = umap[c]; }, r);

	return str;
}
