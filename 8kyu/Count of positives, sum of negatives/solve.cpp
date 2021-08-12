#include <vector>

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
	if (input.empty()) return {};

	int positiveCount = 0;
	int negativeSum = 0;

	for (int x : input)
		if (x > 0)
			positiveCount++;
		else negativeSum += x;

	return {positiveCount, negativeSum};
}
