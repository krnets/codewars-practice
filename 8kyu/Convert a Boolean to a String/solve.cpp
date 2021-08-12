#include <string>
#include <sstream>

std::string boolean_to_string(bool b)
{
	std::ostringstream oss;

	oss << std::boolalpha << b;

	return oss.str();
}
