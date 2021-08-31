#pragma once

std::vector<double> averages(std::vector<int> numbers)
{
	std::vector<double> result;

	for (int i = 1; i < numbers.size(); ++i)
	{
		double x = (numbers[i - 1] + numbers[i]) / 2.0;

		result.push_back(x);
	}

	return result;
}
