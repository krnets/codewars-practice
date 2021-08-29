#pragma once

class SequenceSum
{
	int count;
public:
	SequenceSum(int n) : count(n) { }

	std::string showSequence()
	{
		if (count < 0) return std::to_string(count) + "<0";
		if (count == 0) return "0=0";

		int sum = 0;
		std::string s;

		for (int i = 0; i <= count; ++i)
		{
			s.append(std::to_string(i)).append("+");
			sum += i;
		}
		s.pop_back();
		s.append(" = ").append(std::to_string(sum));

		return s;
	}
};
