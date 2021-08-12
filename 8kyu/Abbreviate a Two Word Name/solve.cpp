#include <string>
#include <sstream>

using namespace std;

/*
string abbrevName(string name)
{
	stringstream ss(name);
	string word;
	string abbrev;

	while (ss >> word)
	{
		abbrev += toupper(word[0]);
		abbrev += '.';
	}

	return abbrev.substr(0, abbrev.size() - 1);
}
*/


string abbrevName(string name)
{
	stringstream ss(name);
	string first, second, abbrev;
	ss >> first >> second;
	abbrev.push_back(toupper(first[0]));
	abbrev.push_back('.');
	abbrev.push_back(toupper(second[0]));

	return abbrev;
}
