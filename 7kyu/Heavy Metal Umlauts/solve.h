#pragma once

using std::string;

string heavyMetalUmlauts(string boringText)
{
	std::map<char, string> umlauts{
		{'A', "Ä"}, {'E', "Ë"}, {'I', "Ï"},
		{'O', "Ö"}, {'U', "Ü"}, {'Y', "Ÿ"},
		{'a', "ä"}, {'e', "ë"}, {'i', "ï"},
		{'o', "ö"}, {'u', "ü"}, {'y', "ÿ"}
	};
	string result;

	for (char& c : boringText)
		if (umlauts.find(c) != umlauts.end())
			result.append(umlauts[c]);
		else result += c;

	return result;
}
