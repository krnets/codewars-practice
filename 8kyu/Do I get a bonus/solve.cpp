#include <string>
#include <sstream>

/*
std::string bonus_time(int salary, bool bonus)
{
	std::string result = "$" + std::to_string(salary);

	return bonus ? result + "0" : result;
}
*/


std::string bonus_time(int salary, bool bonus)
{
	std::ostringstream oss;

	oss << '$' << (bonus ? 10 * salary : salary);

	return oss.str();
}
