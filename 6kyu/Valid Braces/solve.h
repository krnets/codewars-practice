#pragma once

#include <stack>

bool valid_braces(std::string braces)
{
	std::stack<char> stack;
	std::map<char, char> map{{'{', '}'}, {'(', ')'}, {'[', ']'}};

	for (char brace : braces)
	{
		if (map.find(brace) != map.end())
			stack.push(brace);

		else if (!stack.empty() && map[stack.top()] == brace)
			stack.pop();

		else return false;
	}

	return stack.empty();
}
