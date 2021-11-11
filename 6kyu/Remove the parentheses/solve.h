#pragma once

using std::string;

string remove_parentheses(const string& str)
{
	string ans;
	int depth = 0;

	for (char c : str)
	{
		if (c == '(')
			depth++;
		else if (c == ')' && depth > 0)
			depth--;
		else if (depth == 0)
			ans += c;
	}

	return ans;
}
