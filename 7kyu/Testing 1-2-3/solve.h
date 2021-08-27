#pragma once

/*
std::vector<std::string> number(const std::vector<std::string>& lines)
{
	std::vector<std::string> v;

	for (int i = 0; i < lines.size(); ++i)
	{
		v.push_back(std::to_string(i + 1) + ": " + lines.at(i));
	}

	return v;
}
*/

/*
std::vector<std::string> number(const std::vector<std::string>& lines)
{
	auto v = lines;

	for (int i = 0; i < lines.size(); ++i)
	{
		v[i].insert(0, std::to_string(i + 1).append(": "));
	}

	return v;
}
*/

std::vector<std::string> number(const std::vector<std::string>& lines)
{
	std::vector<std::string> v;
	std::transform(lines.begin(), lines.end(), std::back_inserter(v),
	               [i = 1](auto& line) mutable { return std::to_string(i++).append(": ").append(line); });
	return v;
}
