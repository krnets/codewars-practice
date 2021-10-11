#pragma once

/*
int expand_from_middle(const std::string& s, int left, int right)
{
	while (left >= 0 && right < s.length() &&
		s[left] == s[right])
		--left, ++right;

	return right - left + 1;
}
*/

/*
int longest_palindrome(const std::string& s)
{
	if (s.empty()) return 0;

	int start = 0, end = 0;

	for (int i = 0; i < s.length(); ++i)
	{
		int even_pal_len = expand_from_middle(s, i, i);
		int odd_pal_len = expand_from_middle(s, i, i + 1);

		int longest = std::max(even_pal_len, odd_pal_len);

		if (longest > (end - start))
		{
			start = i - (longest - 1) / 2;
			end = i + (longest) / 2;
		}
	}
	return end - start - 1;
}
*/

/*int longest_palindrome(const std::string& s)
{
	if (s.empty()) return 0;

	int longest = 0;

	for (int i = 0; i < s.length(); ++i)
	{
		int even_pal_len = expand_from_middle(s, i, i);
		int odd_pal_len = expand_from_middle(s, i, i + 1);

		longest = std::max(longest, std::max(even_pal_len, odd_pal_len));
	}
	return longest - 2;
}*/

int expand_from_middle(const std::string& s, int left, int right)
{
	while (left >= 0 && right < s.length() &&
		s[left] == s[right])
		--left, ++right;

	return right - left;
}

int longest_palindrome(const std::string& s)
{
	if (s.empty()) return 0;

	int longest = 0;

	for (int i = 0; i < s.length(); ++i)
	{
		int even_pal_len = expand_from_middle(s, i, i);
		int odd_pal_len = expand_from_middle(s, i, i + 1);

		longest = std::max(longest, std::max(even_pal_len, odd_pal_len));
	}
	return longest - 1;
}
