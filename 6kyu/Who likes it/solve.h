#pragma once

using std::string;
using std::vector;

/*
string likes(const vector<string>& names)
{
	std::ostringstream ans;

	switch (names.size())
	{
	case 0:
		ans << "no one likes this";
		break;
	case 1:
		ans << names[0] << " likes this";
		break;
	case 2:
		ans << names[0] << " and " << names[1] << " like this";
		break;
	case 3:
		ans << names[0] << ", " << names[1] << " and " << names[2] << " like this";
		break;
	default:
		ans << names[0] << ", " << names[1] << " and " << names.size() - 2 << " others like this";
	}

	return ans.str();
}
*/

string likes(const vector<string>& names)
{
	std::ostringstream ans;

	switch (names.size())
	{
	case 0:
		ans << "no one";
		break;
	case 1:
		ans << names[0];
		break;
	case 2:
		ans << names[0] << " and " << names[1];
		break;
	case 3:
		ans << names[0] << ", " << names[1] << " and " << names[2];
		break;
	default:
		ans << names[0] << ", " << names[1] << " and " << names.size() - 2 << " others";
	}

	ans << (names.size() <= 1 ? " likes this" : " like this");

	return ans.str();
}
