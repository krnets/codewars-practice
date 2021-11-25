#pragma once

using std::string;

string numberFormat(long long n)
{
	string res = std::to_string(n);

	for (int i = res.length() - 3; i > 0; i -= 3)
	{
		if (res[i - 1] == '-') break;

		res.insert(i, ",");
	}

	return res;
}
