#pragma once

using std::vector;
using std::string;

class Opstrings3
{
public:
	static void split_str(const string& strng, vector<string>& v)
	{
		std::istringstream iss(strng);
		string token;

		while (iss >> token)
			v.push_back(token);
	}

	static string helper(const string& strng, bool dir_reverse)
	{
		vector<string> v;
		split_str(strng, v);
		string res;
		int n = v.size();

		for (int i = 0; i < n; ++i)
			for (int j = i; j < n; ++j)
				std::swap(v[i][j], v[j][i]);

		for (string& s : v)
		{
			if (dir_reverse)
				reverse(s.begin(), s.end());

			res.append(s + '\n');
		}
		res.pop_back();

		return res;
	}

	static string rot90Clock(const string& strng) { return helper(strng, true); }

	static string diag1Sym(const string& strng) { return helper(strng, false); }

	static string selfieAndDiag1(const string& strng)
	{
		vector<string> left, right;
		split_str(strng, left);
		split_str(diag1Sym(strng), right);
		string res;
		int n = left.size();

		for (int i = 0; i < n; ++i)
		{
			res.append(left[i] + '|');
			res.append(right[i] + '\n');
		}
		res.pop_back();

		return res;
	}

	template <typename Func>
	static string oper(Func func, const string& s) { return func(s); }
};
