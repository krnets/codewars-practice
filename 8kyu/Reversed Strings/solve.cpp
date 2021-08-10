#include <string>

using namespace std;

/*
string reverseString(string str)
{
	string result;
	int n = str.length();

	for (int i = n - 1; i >= 0; --i)
	{
		result += str[i];
	}

	return result;
}
*/

string reverseString(string str)
{
	return string(str.rbegin(), str.rend());
}

/*
string reverseString(string str)
{
	reverse(str.begin(), str.end());

	return str;
}
*/
