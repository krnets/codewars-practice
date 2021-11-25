#pragma once

using std::string;

string speedify(const string& input)
{
	auto res = string(125, ' ');

	for (int i = 0; i < input.length(); ++i)
	{
		char c = input[i];
		int jump = c - 'A';

		res[i + jump] = c;
	}

	int pos = res.find_last_not_of(' ') + 1;

	return res.substr(0, pos);
}
