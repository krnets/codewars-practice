#include <string>
#include <algorithm>

/*
std::string DNAtoRNA(std::string dna)
{
	std::string rna;

	for (char c : dna)
		if (c == 'T') rna += 'U';
		else rna += c;

	return rna;
}
*/

std::string DNAtoRNA(std::string dna)
{
	std::replace(dna.begin(), dna.end(), 'T', 'U');
	
	return dna;
}
