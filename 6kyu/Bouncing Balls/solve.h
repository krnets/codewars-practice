#pragma once

/*
class Bouncingball
{
public:
	static int bouncingBall(double h, double bounce, double window)
	{
		if (h <= window || bounce <= 0 || bounce >= 1) return -1;

		return 2 + bouncingBall(h * bounce, bounce, window);
	}
};
*/

class Bouncingball
{
public:
	static int bouncingBall(double h, double bounce, double window)
	{
		if (h <= window || bounce <= 0 || bounce >= 1) return -1;

		int passes = -1;

		while (h > window)
		{
			h *= bounce;
			passes += 2;
		}

		return passes;
	}
};
