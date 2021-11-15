#pragma once

using std::string;

string alphabetized(const string& str)
{
	string ans;

	for (char c : str)
		if (isalpha(c))
			ans += c;

	auto pred = [](char a, char b) { return tolower(a) < tolower(b); };

	stable_sort(ans.begin(), ans.end(), pred);

	return ans;
}
