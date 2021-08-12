/*
int past(int h, int m, int s)
{
	int milliseconds = 1000;
	int seconds = 60;
	int minutes = 60;

	s *= milliseconds;
	m *= seconds * milliseconds;
	h *= minutes * seconds * milliseconds;

	return h + m + s;
}
*/

#include <chrono>

int past(int h, int m, int s)
{
	std::chrono::milliseconds ms{0};

	ms += std::chrono::seconds(s);
	ms += std::chrono::minutes(m);
	ms += std::chrono::hours(h);

	return static_cast<int>(ms.count());
}
