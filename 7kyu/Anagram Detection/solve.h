#pragma once

/*
bool isAnagram(std::string test, std::string original)
{
	int letters[26];
	std::fill(std::begin(letters), std::end(letters), 0);

	for (char c : test)		letters[::tolower(c) - 'a']++;
	for (char c : original) letters[::tolower(c) - 'a']--;

	return std::all_of(std::begin(letters), std::end(letters), [](int x) { return x == 0; });
}
*/


bool isAnagram(std::string test, std::string original)
{
	int letters[26]{0};

	for (char c : test)		letters[::tolower(c) - 'a']++;
	for (char c : original) letters[::tolower(c) - 'a']--;

	return std::all_of(std::begin(letters), std::end(letters), [](int x) { return x == 0; });
}

/*
bool isAnagram(std::string test, std::string original)
{
	int test_char = 0;

	for (char c : test)		test_char ^= (c | 32);
	for (char c : original) test_char ^= (c | 32);

	return test_char == 0;
}
*/
