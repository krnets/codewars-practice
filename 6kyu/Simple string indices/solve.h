#pragma once


int solve(std::string str, int index)
{
	if (str[index] != '(')
		return -1;

	int level = 0;

	for (int i = index; i < str.length(); ++i)
	{
		if (str[i] == '(')
			++level;
		else if (str[i] == ')')
			--level;

		if (level < 0)
			break;
		if (level == 0)
			return i;
	}
	return -1;
}
