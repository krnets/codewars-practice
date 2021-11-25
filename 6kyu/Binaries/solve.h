#pragma once

using std::vector;
using std::string;

namespace coding
{
	vector<string> digit_code{
		"10", "11",
		"0110", "0111",
		"001100", "001101", "001110", "001111",
		"00011000", "00011001"
	};

	string code(const string& strng)
	{
		string res;

		for (char c : strng)
		{
			res += digit_code[c - '0'];
		}
		return res;
	}

	string decode(const string& str)
	{
		int i = str.find('1') + 1;

		if (i == 0) return string();

		int x = stoi(str.substr(i, i), 0, 2);

		return std::to_string(x) + decode(str.substr(i + i));
	}
}
