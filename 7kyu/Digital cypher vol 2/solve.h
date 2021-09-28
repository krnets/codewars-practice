#pragma once

using std::string;
using std::vector;

class Kata
{
public:
	static string Decode(vector<int> code, int n)
	{
		string ans;
		vector<int> digits;

		while (n > 0)
		{
			digits.push_back(n % 10);
			n /= 10;
		}

		int m = digits.size();

		for (int i = 0; i < code.size(); ++i)
		{
			ans += code[i] - digits[m - 1 - i % m] + 'a' - 1;
		}

		return ans;
	}
};
