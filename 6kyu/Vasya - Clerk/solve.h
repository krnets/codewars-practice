#pragma once

/*
std::string tickets(const std::vector<int>& peopleInLine)
{
	std::map<int, int> bills{{25, 0}, {50, 0}, {100, 0}};

	for (auto bill_value : peopleInLine)
	{
		if (bill_value == 25)
			bills[25]++;

		else if (bill_value == 50)
		{
			if (bills[25] == 0)
				return "NO";

			bills[50]++;
			bills[25]--;
		}
		else if (bill_value == 100)
		{
			if (bills[25] == 0)
				return "NO";
			if (bills[50] == 0 && bills[25] < 3)
				return "NO";

			bills[100]++;

			if (bills[50] > 0)
			{
				bills[50]--;
				bills[25]--;
			}
			else
				bills[25] -= 3;
		}
	}

	return "YES";
}
*/

std::string tickets(const std::vector<int>& peopleInLine)
{
	std::map<int, int> bills{{25, 0}, {50, 0}};

	for (auto bill_value : peopleInLine)
	{
		if (bill_value == 25)
			bills[25]++;

		else if (bill_value == 50)
		{
			bills[50]++;
			bills[25]--;
		}
		else if (bill_value == 100)
		{
			if (bills[50] == 0)
				bills[25] -= 3;
			else
			{
				bills[50]--;
				bills[25]--;
			}
		}
		if (bills[25] < 0 || bills[50] < 0) return "NO";
	}

	return "YES";
}
