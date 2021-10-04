#include <vector>
#include <numeric>
// #include <range/v3/all.hpp>

#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/concat.hpp>

using namespace ranges;

/*
int arrayPlusArray(std::vector<int> a, std::vector<int> b)
{
	int sum_a = std::accumulate(a.begin(), a.end(), 0);
	int sum_b = std::accumulate(b.begin(), b.end(), 0);

	return sum_a + sum_b;
}
*/

int arrayPlusArray(std::vector<int> a, std::vector<int> b)
{
	return accumulate(views::concat(a, b), 0);
}
