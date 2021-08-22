#include <cmath>

struct Point
{
	double x;
	double y;
};

/*
double distance_between_two_points(const Point& a, const Point& b)
{
	return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}
*/

double distance_between_two_points(const Point& a, const Point& b)
{
	return std::hypot(a.x - b.x, a.y - b.y);
}
