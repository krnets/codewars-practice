#pragma once

/*
std::string get_middle(std::string input)
{
	bool is_even_length = input.size() % 2 == 0;
	int mid = input.size() / 2;

	return is_even_length ? input.substr(mid - 1, 2) : input.substr(mid, 1);
}
*/

/*
std::string get_middle(std::string input)
{
	size_t width = 2 - input.size() % 2;

	return {input, input.size() / 2 - (width / 2), width};
}
*/

std::string get_middle(std::string input)
{
	int n = input.size();
	int mid = (n - 1) / 2;
	int width = 2 - n % 2;

	return input.substr(mid, width);
}
