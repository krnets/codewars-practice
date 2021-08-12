#include <string>
#include <sstream>

/*
std::string reverse_words(const std::string& str)
{
	std::string result, word;
	int length = 0;

	for (int i = str.size() - 1; i >= 0; --i)
	{
		if (str[i] == ' ')
		{
			word = str.substr(i + 1, length);
			result.append(word);
			result.append(" ");
			length = 0;
		}
		else length++;
	}
	word = str.substr(0, length);
	result.append(word);

	return result;
}
*/

std::string reverse_words(const std::string& str)
{
	std::stringstream ss(str);
	std::string result, word;

	while (ss >> word) result.insert(0, word + ' ');

	result.pop_back();

	return result;
}
