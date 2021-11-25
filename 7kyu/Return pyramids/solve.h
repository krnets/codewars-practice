#pragma once

using std::string;

string pyramid(int n)
{
	std::ostringstream oss;

	for (int i = 0; i < n; ++i)
	{
		string pre = string(n - i - 1, ' ');
		string inside = string(2 * i, (i == n - 1) ? '_' : ' ');

		oss << pre << '/' << inside << '\\' << '\n';
	}
	return oss.str();
}
