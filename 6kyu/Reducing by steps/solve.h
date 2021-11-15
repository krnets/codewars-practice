#pragma once
#include <numeric>

/*
class Operarray
{
public:
	static long long gcdi(long long x, long long y) { return y == 0 ? std::abs(x) : gcdi(y, x % y); }
	static long long lcmu(long long a, long long b) { return std::abs(a * b) / gcdi(a, b); }
	static long long som(long long a, long long b) { return a + b; }
	static long long maxi(long long a, long long b) { return a > b ? a : b; }
	static long long mini(long long a, long long b) { return a < b ? a : b; }

	template <typename Func>
	static long long oper(Func func, long long a, long long b) { return func(a, b); }

	template <typename Func>
	static std::vector<long long> operArray(Func func, std::vector<long long>& arr, long long init)
	{
		std::vector<long long> v;
		v.reserve(arr.size());

		for (auto& x : arr)
		{
			init = oper(func, init, x);
			v.push_back(init);
		}
		return v;
	}
};
*/

class Operarray
{
public:
	static long long gcdi(long long x, long long y) { return y == 0 ? std::abs(x) : gcdi(y, x % y); }
	static long long lcmu(long long a, long long b) { return std::abs(a * b) / gcdi(a, b); }
	static long long som(long long a, long long b) { return a + b; }
	static long long maxi(long long a, long long b) { return a > b ? a : b; }
	static long long mini(long long a, long long b) { return a < b ? a : b; }

	template <class BinaryOperation>
	static std::vector<long long> operArray(BinaryOperation op, std::vector<long long> arr, long long init)
	{
		arr[0] = op(arr[0], init);
		std::partial_sum(arr.begin(), arr.end(), arr.begin(), op);

		return arr;
	}
};
