#pragma once

using std::string;

string sortMyString(const string& s)
{
	string ans;

	for (int i = 0; i < s.length(); i += 2) ans += s[i];

	ans.append(" ");

	for (int i = 1; i < s.length(); i += 2) ans += s[i];

	return ans;
}
