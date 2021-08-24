#pragma once

bool XO(const std::string& str)
{
	int countX = 0;
	int countO = 0;

	for (char c : str)
	{
		if (::toupper(c) == 'X')
			countX++;
		else if (::toupper(c) == 'O')
			countO++;
	}

	return countX == countO;
}
