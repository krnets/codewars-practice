#pragma once
#include <bitset>

using std::string;
using std::bitset;

string encode(string text)
{
	string bits;

	for (char c : text)
		for (char ch : bitset<8>(c).to_string())
			bits.append(string(3, ch));

	return bits;
}

string decode(string bits)
{
	string text;

	for (int i = 0; i < bits.length(); i += 24)
	{
		string s = bits.substr(i, 24);
		char c = 0;

		for (int j = 0; j < s.length(); j += 3)
		{
			string sub = s.substr(j, 3);
			int cnt = bitset<3>(stoi(sub)).count();
			c <<= 1;

			if (cnt > 1)
				c ^= 1;
		}
		text += c;
	}
	return text;
}
