#pragma once
#include <string>
#include <unordered_map>
#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

/*
std::string DNAStrand(const std::string& dna)
{
	std::unordered_map<char, char> umap{
		{'A', 'T'},
		{'C', 'G'},
		{'T', 'A'},
		{'G', 'C'}
	};
	std::string ans(dna);
	std::transform(ans.begin(), ans.end(), ans.begin(), [umap](char c) { return umap.at(c); });

	return ans;
}
*/

using std::string;

string DNAStrand(const string& dna)
{
	std::unordered_map<char, char> umap{
		{'A', 'T'},
		{'C', 'G'},
		{'T', 'A'},
		{'G', 'C'}
	};

	return dna
		| ranges::views::transform([&](char c) { return umap[c]; })
		| ranges::to<string>();
}
