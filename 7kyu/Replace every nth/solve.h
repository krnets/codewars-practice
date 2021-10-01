#pragma once

class Kata
{
public:
	std::string replaceNth(std::string text, int n, char oldValue, char newValue)
	{
		if (n <= 0)
			return text;

		int index = 0;

		for (char& c : text)
		{
			if (c == oldValue)
			{
				index++;

				if (index % n == 0)
				{
					c = newValue;
				}
			}
		}

		return text;
	}
};
