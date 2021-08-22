#include <string>
#include <vector>

/*
int digitSum(int n)
{
	int sum = 0;

	while (n != 0)
	{
		sum += n % 10;
		n /= 10;
	}

	return sum;
};

std::string SubtractSum(int n)
{
	std::vector<std::string> v{
		"kiwi", "pear", "kiwi", "banana", "melon", "banana", "melon", "pineapple", "apple", "pineapple", "cucumber",
		"pineapple", "cucumber", "orange", "grape", "orange", "grape", "apple", "grape", "cherry", "pear", "cherry",
		"pear", "kiwi", "banana", "kiwi", "apple", "melon", "banana", "melon", "pineapple", "melon", "pineapple",
		"cucumber", "orange", "apple", "orange", "grape", "orange", "grape", "cherry", "pear", "cherry", "pear",
		"apple", "pear", "kiwi", "banana", "kiwi", "banana", "melon", "pineapple", "melon", "apple", "cucumber",
		"pineapple", "cucumber", "orange", "cucumber", "orange", "grape", "cherry", "apple", "cherry", "pear", "cherry",
		"pear", "kiwi", "pear", "kiwi", "banana", "apple", "banana", "melon", "pineapple", "melon", "pineapple",
		"cucumber", "pineapple", "cucumber", "apple", "grape", "orange", "grape", "cherry", "grape", "cherry", "pear",
		"cherry", "apple", "kiwi", "banana", "kiwi", "banana", "melon", "banana", "melon", "pineapple", "apple",
		"pineapple"
	};

	n = n - digitSum(n);

	while (n > 100)
	{
		n = n - digitSum(n);
	}

	return v.at(n - 1);
}
*/

#define 🍎 "apple"

std::string SubtractSum(int n)
{
	if (n == 0) return "n - n mod 9 = 0";

	return 🍎;
}
