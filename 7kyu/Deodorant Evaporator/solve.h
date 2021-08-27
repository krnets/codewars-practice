#pragma once

/*
class Evaporator
{
public:
	static int evaporator(double content, double evap_per_day, double threshold)
	{
		int day = 0;
		double out_of_use = content * (threshold / 100);
		double reduce_by = (100 - evap_per_day) / 100;

		while (content >= out_of_use)
		{
			content *= reduce_by;
			day++;
		}

		return day;
	}
};
*/

class Evaporator
{
public:
	static int evaporator(double content, double evap_per_day, double threshold)
	{
		return int(ceil(log(threshold / 100) / log(1.0 - evap_per_day / 100)));
	}
};
