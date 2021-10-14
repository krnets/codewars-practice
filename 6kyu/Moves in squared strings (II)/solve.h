#pragma once

#include <range/v3/algorithm/reverse.hpp>
#include <range/v3/view/join.hpp>
#include <range/v3/view/reverse.hpp>
#include <range/v3/view/tokenize.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;
using std::vector;

class Opstrings1
{
public:
	static string rot(const string& strng)
	{
		return strng | views::reverse | to<string>();
	}

	static string selfieAndRot(const string& strng)
	{
		vector<string> vs1 = strng
			| views::tokenize(std::regex{"\\S+"})
			| views::transform([](string&& s) { return s + string(s.length(), '.'); })
			| to<vector<string>>();

		vector<string> vs2 = vs1
			| views::transform([&](auto&& s) { return rot(s); })
			| to<vector<string>>();

		reverse(vs2);

		string ret1 = vs1 | views::join('\n') | to<string>();
		string ret2 = vs2 | views::join('\n') | to<string>();

		return ret1 + '\n' + ret2;
	}

	template <typename Func>
	static string oper(Func func, const string& s)
	{
		return func(s);
	}
};
