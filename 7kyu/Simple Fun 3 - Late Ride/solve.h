#pragma once


int lateRide(int n)
{
	int hh = n / 60;
	int mm = n % 60;
	int ans = 0;

	while (hh > 0)
	{
		ans += hh % 10;
		hh /= 10;
	}

	while (mm > 0)
	{
		ans += mm % 10;
		mm /= 10;
	}

	return ans;
}
