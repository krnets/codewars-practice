#pragma once

/*
class SqInRect
{
public:
	static std::vector<int> sqInRect(int lng, int wdth)
	{
		std::vector<int> v;

		if (lng == wdth)
			return v;

		while (lng * wdth > 0)
		{
			if (lng > wdth)
			{
				v.push_back(lng - (lng - wdth));
				lng -= wdth;
			}
			else
			{
				v.push_back(wdth - (wdth - lng));
				wdth -= lng;
			}
		}
		return v;
	}
};
*/

class SqInRect
{
public:
	static std::vector<int> sqInRect(int lng, int wdth)
	{
		std::vector<int> v;

		if (lng == wdth)
			return v;

		while (lng * wdth > 0)
		{
			if (lng > wdth)
			{
				v.push_back(wdth);
				lng -= wdth;
			}
			else
			{
				v.push_back(lng);
				wdth -= lng;
			}
		}

		return v;
	}
};
