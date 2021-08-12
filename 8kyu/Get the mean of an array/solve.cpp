#include <vector>
#include <numeric>

/*
int get_average(std::vector <int> marks)
{
	int sum = 0;

	for (int mark : marks) sum += mark;

	return sum / marks.size();
}
*/


int get_average(std::vector<int> marks)
{
	return std::accumulate(marks.begin(), marks.end(), 0) / marks.size();
}
