#pragma once
#include <regex>

using std::string;

string covfefe(string s)
{
	const string coverage = "coverage";
	const string covfefe = "covfefe";

	if (s.find(coverage) == string::npos)
		return s + " " + covfefe;

	size_t pos = 0;

	while ((pos = s.find(coverage, pos)) != string::npos)
	{
		s.replace(pos, coverage.length(), covfefe);
		pos += covfefe.length();
	}

	return s;
}

/*
string covfefe(string s)
{
	return std::regex_match(s, std::regex(".*coverage.*"))
		       ? std::regex_replace(s, std::regex("coverage"), "covfefe")
		       : s + " covfefe";
}
*/
