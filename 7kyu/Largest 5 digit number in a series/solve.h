#pragma once

int largest_five_digits(const std::string& digits)
{
	int max = std::numeric_limits<int>::min();

	for (size_t i = 0; i < digits.size() - 4; ++i)
	{
		auto sub = digits.substr(i, 5);

		max = std::max(max, std::stoi(sub));
	}

	return max;
}
