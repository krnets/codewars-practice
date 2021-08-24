#pragma once
#include <string>
#include <unordered_map>

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
