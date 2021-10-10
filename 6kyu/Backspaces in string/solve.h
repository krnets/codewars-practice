#pragma once

using std::string;

string cleanString(const string& s)
{
	string ans;

	for (char c : s)
	{
		if (c == '#')
		{
			if (!ans.empty())
				ans.pop_back();
		}
		else ans.push_back(c);
	}
	return ans;
}

/*
string cleanString(const string& s)
{
	string ans;

	for (char c : s)
	{
		if (c != '#')
			ans.push_back(c);
		else if (!ans.empty())
			ans.pop_back();
	}
	return ans;
}
*/
