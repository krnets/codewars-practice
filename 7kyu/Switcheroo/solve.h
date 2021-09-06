#pragma once

/*
std::string switcheroo(const std::string& s)
{
	std::string ans;

	for (char c : s)
	{
		if (c == 'a')
			ans += 'b';
		else if (c == 'b')
			ans += 'a';
		else ans += c;
	}

	return ans;
}
*/

std::string switcheroo(const std::string& s)
{
	std::string ans = s;
	std::transform(ans.begin(), ans.end(), ans.begin(), [](char c)
	{
		return c == 'a' ? 'b' : c == 'b' ? 'a' : c;
	});

	return ans;
}
