#pragma once

/*
std::string arithmeticSequenceElements(int a, int r, int n)
{
	std::string s;

	for (int i = 0; i < n; ++i)
	{
		s += std::to_string(a) + ", ";
		a += r;
	}

	return s.substr(0, s.length() - 2);
}
*/

/*
std::string arithmeticSequenceElements(int a, int r, int n)
{
	std::string s;

	while (n > 0)
	{
		s += std::to_string(a) + ", ";
		a += r;
		--n;
	}

	return s.substr(0, s.length() - 2);
}
*/

std::string arithmeticSequenceElements(int a, int r, int n)
{
	std::string s = std::to_string(a);

	while (--n)
	{
		a += r;
		s.append(", " + std::to_string(a));
	}

	return s;
}
