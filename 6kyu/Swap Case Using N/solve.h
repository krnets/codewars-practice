#pragma once
#include <bitset>

using std::string;

string swapp(string s, int n)
{
	if (n == 0) return s;

	string bits = std::bitset<32>(n).to_string();

	int pos = bits.find_first_of('1');
	bits = bits.substr(pos);
	int len = bits.length();
	pos = 0;

	for (char& c : s)
		if (isalpha(c))
		{
			if (bits[pos % len] == '1')
				c ^= 32;

			++pos;
		}

	return s;
}
