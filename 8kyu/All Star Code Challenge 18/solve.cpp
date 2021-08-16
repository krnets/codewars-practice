#include <string>
#include <algorithm>

/*
unsigned int strCount(std::string word, char letter)
{
	unsigned count = 0;;

	for (char c : word)
		if (c == letter)
			count++;

	return count;
}
*/

/*
unsigned int strCount(std::string word, char letter)
{
	return count_if(word.begin(), word.end(), [letter](char c) { return c == letter; });
}
*/

unsigned int strCount(std::string word, char letter)
{
	return count(word.begin(), word.end(), letter);
}
