#pragma once

/*
int circleOfNumbers(int n, int firstNumber)
{
	int ans = n - (n / 2) + firstNumber;

	return ans < n ? ans : ans - n;
}
*/

int circleOfNumbers(int n, int firstNumber)
{
	return (firstNumber + n / 2) % n;
}
