/*
#include <vector>

std::vector<int> digitize(long long n)
{
	std::vector<int> ans;

	while (n > 0)
	{
		ans.push_back(n % 10);
		n /= 10;
	}

	return ans;
}
*/


#include <vector>
#include <sstream>

std::vector<int> digitize(long long n)
{
	std::ostringstream os;
	os << n;

	std::string digits_str = os.str();

	std::vector<int> digits;

	for (int i = digits_str.size() - 1; i >= 0; --i)
	{
		int x = digits_str[i] - '0';

		digits.push_back(x);
	}

	return digits;
}
