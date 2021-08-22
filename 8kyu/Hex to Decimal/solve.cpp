#include <string>
#include <sstream>

/*int hexToDec(std::string hexString)
{
	int ans = 0;
	std::stringstream ss;
	ss << std::hex << hexString;
	ss >> ans;

	return ans;
}*/

/*
int hexToDec(std::string hexString)
{
	int ans = 0;
	ans = std::stoi(hexString, nullptr, 16);

	return ans;
}
*/

int hexToDec(std::string hexString)
{
	return std::stoi(hexString, 0, 16);
}
