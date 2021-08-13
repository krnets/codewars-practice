#include <string>
#include <algorithm>

/*
std::string makeUpperCase(const std::string& input_str)
{
	std::string result;

	for (char c : input_str)
		if (c > 'Z')
			result += c - 32;
		else result += c;

	return result;
}
*/

/*
std::string makeUpperCase(const std::string& input_str)
{
	std::string output_str = input_str;
	std::transform(output_str.begin(), output_str.end(), output_str.begin(),
	               [](char c) { return c > 'Z' ? c - 32 : c; });
	
	return output_str;
}
*/


std::string makeUpperCase(const std::string& input_str)
{
	std::string output_str = input_str;
	transform(output_str.begin(), output_str.end(), output_str.begin(), toupper);

	return output_str;
}
