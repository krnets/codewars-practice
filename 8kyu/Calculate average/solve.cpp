#include <vector>
#include <numeric>

/*
double calcAverage(const std::vector<int>& values)
{
	return std::accumulate(values.begin(), values.end(), 0) / static_cast<double>(values.size());
}
*/

double calcAverage(const std::vector<int>& values)
{
	return std::accumulate(values.begin(), values.end(), 0.0) / values.size();
}
