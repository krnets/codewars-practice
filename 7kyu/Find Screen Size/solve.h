#pragma once

#include <cmath>
#include <string>
#include <fmt/core.h>

using namespace std;

/*
string find_screen_height(int width, const string& ratio)
{
	istringstream iss(ratio);
	ostringstream oss;
	string s;
	vector<string> v;

	while (getline(iss, s, ':'))
	{
		v.push_back(s);
	}

	double x = stoi(v[0]);
	double y = stoi(v[1]);

	oss << width << "x" << floor(width / x * y);

	return oss.str();
}
*/


std::string find_screen_height(int width, const std::string& ratio)
{
	int x = std::stoi(ratio);
	int y = std::stoi(ratio.substr(ratio.find(':') + 1));

	return fmt::format("{}x{}", width, width * y / x);
}
