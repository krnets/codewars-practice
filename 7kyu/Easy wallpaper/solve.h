#pragma once

#include <cmath>

using namespace std;

class Wallpaper
{
	constexpr static double roll_width = 52;
	constexpr static double roll_length = 1000;
	constexpr static double roll_extra_percent = 15;

	inline const static vector<string> numbers_{
		"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
		"twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
	};

public:
	static string wallPaper(double length, double width, double height)
	{
		if (length * width * height == 0)
			return numbers_[0];

		double s = 2 * width * height + 2 * length * height;
		double k = s / (roll_width * 100 / roll_length);
		double extra = (100 + roll_extra_percent) / 100;
		k = ceil(k * extra);

		return numbers_[k];
	}
};
