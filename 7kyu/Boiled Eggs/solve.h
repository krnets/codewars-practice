#pragma once

#include <cmath>

unsigned int cookingTime(unsigned int eggs)
{
	return 5 * ceil(eggs / 8.0);
}
