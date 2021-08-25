#pragma once

/*
std::string reverse_words(std::string str)
{
	std::string result;
	const size_t length = str.size();
	result.reserve(length);

	int wordStart = 0;

	for (int i = 0; i < length; ++i)
	{
		if (str[i] == ' ')
		{
			for (int j = i - 1; j >= wordStart; --j)
				result.push_back(str[j]);

			result.push_back(str[i]);
			wordStart = i + 1;
		}
	}

	if (wordStart < length)
		for (int j = length - 1; j >= wordStart; --j)
			result.push_back(str[j]);

	return result;
}
*/

/*
std::string reverse_words(std::string str)
{
	auto wordBegin = str.begin();

	for (auto iter = str.begin(); iter < str.end(); ++iter)
	{
		if (*iter == ' ')
		{
			std::reverse(wordBegin, iter);
			wordBegin = iter + 1;
		}
	}

	std::reverse(wordBegin, str.end());

	return str;
}
*/

std::string reverse_words(std::string str)
{
	std::string out, word;

	for (char c : str)
	{
		if (c == ' ')
		{
			out.append(word + c);
			word.clear();
			continue;
		}
		word.insert(0, 1, c);
	}

	return out + word;
}
