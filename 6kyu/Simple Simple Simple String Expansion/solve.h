#pragma once

using std::string;

/*
string string_expansion(const string& s)
{
	string ans;

	for (int i = 0; i < s.length(); ++i)
	{
		if (isdigit(s[i]))
		{
			int x = s[i] - '0';
			int j = i;

			while (isalpha(s[j + 1])) ++j;

			int dist = j - i;

			if (dist > 0)
			{
				string t = s.substr(i + 1, dist);

				for (char c : t)
					ans.append(string(x, c));
			}
			i = j;
		}
		else ans += s[i];
	}

	return ans;
}
*/

string string_expansion(const string& s)
{
	string ans;
	int repeat = 1;

	for (char c : s)
		if (isdigit(c))
			repeat = c - '0';
		else ans += string(repeat, c);

	return ans;
}
