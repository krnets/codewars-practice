#pragma once

#include <numeric>

/*
class Opstrings
{
public:
	static std::string vertMirror(const std::string& strng);
	static std::string horMirror(const std::string& strng);

	template <typename Func>
	static std::string oper(Func func, const std::string& s)
	{
		return func(s);
	}

private:
	static std::vector<std::string> split(const std::string& strng);
};

auto Opstrings::split(const std::string& strng) -> std::vector<std::string>
{
	std::vector<std::string> words;
	std::istringstream iss(strng);
	std::string word;

	while (iss >> word) words.push_back(word);

	return words;
}

inline auto Opstrings::vertMirror(const std::string& strng) -> std::string
{
	auto words = split(strng);
	std::string ans;

	for (auto word : words)
	{
		std::reverse(word.begin(), word.end());
		ans.append(word).append("\n");
	}
	ans.pop_back();

	return ans;
}

inline auto Opstrings::horMirror(const std::string& strng) -> std::string
{
	auto words = split(strng);
	std::string ans = std::accumulate(words.rbegin(), words.rend(), std::string(),
	                                  [](std::string a, std::string b) { return a.append("\n").append(b); });
	return ans.substr(1);
}
*/

/*
auto Opstrings::split(const std::string& strng) -> std::vector<std::string>
{
	std::vector<std::string> words;
	std::istringstream iss(strng);

	for (std::string word; std::getline(iss, word);)
		words.push_back(word);

	return words;
}
*/

class Opstrings
{
public:
	static std::string vertMirror(const std::string& strng);
	static std::string horMirror(const std::string& strng);

	template <typename Func>
	static std::string oper(Func fn, const std::string& s)
	{
		return fn(s);
	}

private:
	static std::vector<std::string> split(const std::string& strng);
	static std::string join(const std::vector<std::string>& v);
};

auto Opstrings::split(const std::string& strng) -> std::vector<std::string>
{
	std::vector<std::string> vec;
	std::istringstream iss(strng);

	for (std::string word; std::getline(iss, word);)
		vec.push_back(word);

	return vec;
}

inline auto Opstrings::join(const std::vector<std::string>& v) -> std::string
{
	std::string ans;

	for (auto s : v)
		ans.append(s).append("\n");

	return ans.erase(ans.size() - 1);
}

inline auto Opstrings::vertMirror(const std::string& strng) -> std::string
{
	auto vec = split(strng);

	for (auto& s : vec)
		std::reverse(s.begin(), s.end());

	return join(vec);
}

inline auto Opstrings::horMirror(const std::string& strng) -> std::string
{
	auto vec = split(strng);
	std::reverse(vec.begin(), vec.end());

	return join(vec);
}
