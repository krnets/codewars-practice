#pragma once

/*
int growingPlant(int upSpeed, int downSpeed, int desiredHeight)
{
	int countDays = 0;
	int plantHeight = 0;

	while (plantHeight < desiredHeight)
	{
		plantHeight += upSpeed;
		countDays++;

		if (plantHeight >= desiredHeight)
			return countDays;

		plantHeight -= downSpeed;
	}

	return countDays;
}
*/

int growingPlant(int upSpeed, int downSpeed, int desiredHeight)
{
	int countDays = 1;
	int plantHeight = upSpeed;

	while (plantHeight < desiredHeight)
	{
		plantHeight += (upSpeed - downSpeed);
		countDays++;
	}

	return countDays;
}
