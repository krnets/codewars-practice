#include <vector>
#include <numeric>

bool betterThanAverage(std::vector<int> classPoints, int yourPoints)
{
	int classAverage = std::accumulate(classPoints.begin(), classPoints.end(), 0) / classPoints.size();

	return yourPoints > classAverage;
}
