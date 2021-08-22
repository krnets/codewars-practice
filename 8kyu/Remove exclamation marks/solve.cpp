#include <regex>
#include <string>

/*
std::string removeExclamationMarks(std::string str)
{
	std::string ans;

	for (char c : str)
		if (c != '!')
			ans += c;

	return ans;
}
*/

/*
std::string removeExclamationMarks(std::string str)
{
	std::regex e("!");

	return std::regex_replace(str, e, "");
}
*/

/*
std::string removeExclamationMarks(std::string str)
{
	str.erase(std::remove(str.begin(), str.end(), '!'), str.end());

	return str;
}
*/


/*
std::string removeExclamationMarks(std::string str)
{
	std::vector<char> stage;

	for (char c : str)
		if (c != '!')
			stage.push_back(c);

	return std::string(stage.begin(), stage.end());
}
*/

std::string removeExclamationMarks(std::string str)
{
	std::string ans;

	for (char c : str)
		if (c != '!')
			ans.push_back(c);

	return ans;
}
