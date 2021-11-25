#pragma once

using std::vector;

std::pair<double, double> cog_rpm(const vector<int>& cogs, int n)
{
	int gears = cogs.size() - 1;

	vector clockwiseRotation{1.0, -1.0};

	double firstCogRPM = cogs[n] * clockwiseRotation[n & 1] / cogs.front();
	double lastCogRPM = cogs[n] * clockwiseRotation[(gears - n) & 1] / cogs[gears];

	return std::make_pair(firstCogRPM, lastCogRPM);
}
