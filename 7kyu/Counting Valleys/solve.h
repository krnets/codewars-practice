#pragma once

int countValleys(const std::string& s)
{
	int level = 0;
	int prev = 0;
	int count = 0;

	for (char c : s)
	{
		if (c == 'U') ++level;
		else if (c == 'D') --level;

		if (level == 0 && prev < 0)
			++count;

		prev = level;
	}

	return count;
}
