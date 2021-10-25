#pragma once

using std::string;

int deleteDigit(int n)
{
	string s = std::to_string(n);
	int max = 0;

	for (int i = 0; i < 10; ++i)
	{
		char c = '0' + i;

		if (s.find(c) != string::npos)
		{
			int pos = s.find_first_of(c);
			string t = s;
			t.erase(t.begin() + pos, t.begin() + pos + 1);
			int m = std::stoi(t);

			if (m > max)
				max = m;
		}
	}
	return max;
}
