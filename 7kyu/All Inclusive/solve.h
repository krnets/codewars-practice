#pragma once

class Rotations
{
public:
	static bool containAllRots(const std::string& strng, std::vector<std::string>& arr)
	{
		auto rs = strng;

		for (int i = 0; i < strng.length(); ++i)
		{
			if (std::ranges::none_of(arr, [rs](auto s) { return s == rs; }))
				return false;

			std::ranges::rotate(rs, rs.begin() + 1);
		}

		return true;
	}
};
