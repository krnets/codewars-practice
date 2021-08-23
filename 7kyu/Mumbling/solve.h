#pragma once

/*
class Accumul
{
public:
	static std::string accum(const std::string& s)
	{
		std::string result;
		int n = s.size();

		for (int i = 0; i < n; ++i)
		{
			char c = s[i];
			result.push_back(std::toupper(c));

			if (i > 0)
			{
				for (int j = 1; j <= i; ++j)
				{
					result.push_back(std::tolower(c));
				}
			}

			result.push_back('-');
		}

		return result.substr(0, result.size() - 1);
	}
};
*/

class Accumul
{
public:
	static std::string accum(const std::string& s)
	{
		std::ostringstream oss;
		int n = s.size();

		for (int i = 0; i < n; ++i)
		{
			oss << "-" << std::string(1, ::toupper(s[i])) << std::string(i, ::tolower(s[i]));
		}

		return oss.str().substr(1);
	}
};
