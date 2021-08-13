#include <string>
#include <stdexcept>

std::string bmi(double w, double h)
{
	double calc = w / h / h;

	return (calc <= 18.5) ? "Underweight" : (calc <= 25.0) ? "Normal" : (calc <= 30.0) ? "Overweight" : "Obese";
}
