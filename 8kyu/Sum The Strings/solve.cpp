#include <string>
#include <sstream>

/*
std::string sum_str(const std::string& a, const std::string& b)
{
	int x = a.empty() ? 0 : std::stoi(a);
	int y = b.empty() ? 0 : std::stoi(b);

	int n = x + y;

	return std::to_string(n);
}
*/

/*
std::string sum_str(const std::string& a, const std::string& b)
{
	int x = std::atoi(std::string_view(a).data());
	int y = std::atoi(std::string_view(b).data());

	int n = x + y;

	return std::to_string(n);
}
*/

std::string sum_str(const std::string& a, const std::string& b)
{
	int x = 0, y = 0;
	std::istringstream(a) >> x;
	std::istringstream(b) >> y;

	int n = x + y;

	return std::to_string(n);
}

