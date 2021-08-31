#pragma once

unsigned int countRedBeads(unsigned int n)
{
	return n == 0 ? 0 : 2 * (n - 1);
}
