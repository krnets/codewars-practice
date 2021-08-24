#pragma once

/*
class Arge
{
public:
	static int nbYear(int p0, double percent, int aug, int p)
	{
		int countYears = 0;

		while (p0 < p)
		{
			p0 = p0 * (1 + percent / 100.0) + aug;
			countYears++;
		}

		return countYears;
	}
};
*/

class Arge
{
public:
	static int nbYear(int p0, double percent, int aug, int p);
};

inline int Arge::nbYear(int p0, double percent, int aug, int p)
{
	return p0 < p ? 1 + nbYear(p0 * (1 + percent / 100.0) + aug, percent, aug, p) : 0;
}
