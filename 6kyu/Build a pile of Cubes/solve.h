#pragma once

class ASum
{
public:
	static long long findNb(long long m)
	{
		long long level = 1;
		long long cubeSum = 0;

		while (cubeSum < m)
		{
			cubeSum += (level * level * level);
			++level;
		}

		return cubeSum == m ? level - 1 : -1;
	}
};
