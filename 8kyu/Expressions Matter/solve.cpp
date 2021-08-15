#include <algorithm>
#include <vector>

/*
unsigned short int expressionsMatter(unsigned short a, unsigned short b, unsigned short c)
{
	unsigned short combo1 = a + b + c;
	unsigned short combo2 = a * b * c;
	unsigned short combo3 = a * (b + c);
	unsigned short combo4 = (a + b) * c;

	std::vector v{combo1, combo2, combo3, combo4};

	return *std::max_element(v.begin(), v.end());
}
*/

unsigned short int expressionsMatter(unsigned short int a, unsigned short int b, unsigned short int c)
{
	return std::max({a + b + c, a * b * c, (a + b) * c, a * (b + c)});
}
