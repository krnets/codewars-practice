#include <string>
#include <sstream>

std::string integrate(const int& coefficient, const int& exponent)
{
	std::ostringstream oss;

	oss << coefficient / (exponent + 1) << "x^" << exponent + 1;

	return oss.str();
}
