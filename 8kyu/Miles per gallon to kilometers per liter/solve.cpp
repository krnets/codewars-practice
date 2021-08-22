#include <cmath>

double converter(int mpg)
{
	double litresInImperialGallon = 4.54609188;
	double kmInMile = 1.609344;
	double ans = mpg * kmInMile / litresInImperialGallon;

	return round(ans * 100) / 100;
}
