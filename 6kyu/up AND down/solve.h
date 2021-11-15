#pragma once

using std::string;

class UpAndDown
{
public:
	static string arrange(const string& strng)
	{
		if (strng.empty()) return strng;

		std::istringstream iss(strng);
		string result, word;
		std::vector<string> words;

		while (iss >> word)
			words.push_back(word);

		for (int i = 0; i < words.size() - 1; ++i)
			if (words[i + i % 2].length() > words[i + 1 - i % 2].length())
				swap(words[i], words[i + 1]);

		for (int i = 0; i < words.size(); ++i)
		{
			if (i % 2 == 0)
				for (char& c : words[i])
					result += tolower(c);
			else
				for (char& c : words[i])
					result += toupper(c);

			result += ' ';
		}
		result.pop_back();

		return result;
	}
};
