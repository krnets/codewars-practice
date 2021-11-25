#pragma once
#include <iomanip>

using namespace std;

string hist(const string& s)
{
	vector<int> freq(128);

	for (char c : s)
		freq[c]++;

	bool first = true;
	ostringstream oss;
	string error_chars = "uwxz";

	for (char c : error_chars)
	{
		if (freq[c])
		{
			if (!first)
				oss << "\\r";

			oss << left << c << "  " << setw(6) << freq[c] << string(freq[c], '*');
			first = false;
		}
	}
	return oss.str();
}
