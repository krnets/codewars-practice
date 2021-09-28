#pragma once

using std::string;

/*
class ScalingSqStrings
{
public:
	static string scale(const string& strng, int k, int n)
	{
		string line;
		std::istringstream iss(strng);
		std::ostringstream oss;
		std::vector<string> v;

		while (iss >> line)
		{
			string temp;

			for (char c : line)
				temp.append(k, c);

			for (int i = 0; i < n; ++i)
				oss << temp << "\n";
		}
		string ans = oss.str();

		return ans.substr(0, ans.length() - 1);
	}
};
*/

class ScalingSqStrings
{
public:
	static string scale(const string& strng, int k, int n)
	{
		string ans, line;
		std::istringstream iss(strng);

		while (std::getline(iss, line))
			for (int i = 0; i < n; ++i)
			{
				for (char c : line)
					ans.append(k, c);

				ans.push_back('\n');
			}

		return ans.substr(0, ans.length() - 1);
	}
};
