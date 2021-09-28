#pragma once

using std::string;

/*
string flyBy(string lamp, string drone)
{
	int pos = drone.find('T') + 1;

	std::transform(lamp.begin(), lamp.begin() + pos, lamp.begin(), [](char) { return 'o'; });

	return lamp;
}
*/

using std::string;

string flyBy(string lamp, string drone)
{
	return lamp.replace(0, drone.length(), drone.length(), 'o');
}
