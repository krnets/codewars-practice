#pragma once

using std::string;

/*
string solve(const string& s, unsigned k)
{
	string ans(s);

	for (char c = 'a'; c <= 'z'; ++c)
	{
		while (k > 0 && ans.find(c) != string::npos)
		{
			ans.erase(ans.find(c), 1);
			--k;
		}
		if (k == 0) break;
	}

	return ans;
}
*/

/*
string solve(const string& s, unsigned k)
{
	string ans(s);

	for (char c = 'a'; c <= 'z'; ++c)
	{
		size_t pos = ans.find(c);

		while (k > 0 && pos != string::npos)
		{
			ans.erase(ans.find(c), 1);
			pos = ans.find(c);
			--k;
		}
		if (k == 0) break;
	}

	return ans;
}
*/

string solve(const string& s, unsigned k)
{
	string ans(s);
	k = std::min<int>(k, s.length());
	char c = 'a';

	while (k > 0)
	{
		size_t pos = ans.find(c);

		if (pos == string::npos)
			++c;
		else
		{
			ans.erase(pos, 1);
			--k;
		}
	}

	return ans;
}
