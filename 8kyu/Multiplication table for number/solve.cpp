#include <string>
#include <vector>
#include <numeric>
#include <sstream>

/*
std::string multi_table(int number)
{
	std::vector<std::string> vec;

	for (int i = 1; i <= 10; ++i)
	{
		std::stringstream ss;
		ss << i << " * " << number << " = " << i * number;

		vec.push_back(ss.str());
	}

	std::string ans = std::accumulate(vec.begin(), vec.end(), std::string(""),
	                                  [](const std::string a, const std::string b) { return a + "\n" + b; });

	return ans.substr(1, ans.size() - 1);
}
*/

std::string multi_table(int number)
{
	std::ostringstream ss;

	for (int i = 1; i <= 10; ++i)
	{
		ss << i << " * " << number << " = " << i * number << (i < 10 ? "\n" : "");
	}

	return ss.str();
}
