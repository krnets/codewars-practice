#pragma once

using std::string;

string solve(int n)
{
	string a = "0";
	string b = "01";

	while (n--)
	{
		string temp = a;
		a = b;
		b = b + temp;
	}
	return a;
}
