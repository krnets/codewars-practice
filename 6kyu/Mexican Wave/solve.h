#pragma once

using std::string;
using std::vector;

/*
vector<string> wave(string s)
{
	vector<string> v;

	for (int i = 0; i < s.length(); ++i)
	{
		if (s[i] == ' ') continue;

		string modified(s);
		modified[i] = toupper(modified[i]);
		v.push_back(modified);
	}

	return v;
}
*/

/*
vector<string> wave(string s)
{
	vector<string> v;

	for (int i = 0; i < s.length(); ++i)
	{
		if (isspace(s[i])) continue;

		string modified(s);
		modified[i] = toupper(modified[i]);
		v.push_back(modified);
	}

	return v;
}
*/

vector<string> wave(string s)
{
	vector<string> v;

	for (int i = 0; i < s.length(); ++i)
	{
		if (!isspace(s[i]))
		{
			string modified(s);
			modified[i] = toupper(modified[i]);
			v.push_back(modified);
		}
	}
	return v;
}
