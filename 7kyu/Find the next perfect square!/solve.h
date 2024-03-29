﻿#pragma once
#include <cmath>

long long findNextSquare(long long sq)
{
	auto root = sqrt(sq) + 1;

	if (fmodl(root, 1) != 0)
		return -1;

	return root * root;
}
