#pragma once

/*
std::string alphabetWar(std::string fight)
{
	int leftScore = 0;
	int rightScore = 0;

	std::vector<char> leftPower{'s', 'b', 'p', 'w'};
	std::vector<char> rightPower{'z', 'd', 'q', 'm'};

	for (char c : fight)
	{
		auto leftIter = std::find(leftPower.begin(), leftPower.end(), c);
		auto rightIter = std::find(rightPower.begin(), rightPower.end(), c);

		if (leftIter != leftPower.end())
		{
			leftScore += leftIter - leftPower.begin() + 1;
		}
		else if (rightIter != rightPower.end())
		{
			rightScore += rightIter - rightPower.begin() + 1;
		}
	}

	std::string winner = (leftScore > rightScore ? "Left" : "Right");

	return leftScore == rightScore ? "Let's fight again!" : winner + " side wins!";
}
*/

std::string alphabetWar(std::string fight)
{
	int score = 0;

	std::string left = " sbpw";
	std::string right = " zdqm";

	for (char c : fight)
	{
		auto iter_l = std::find(left.begin(), left.end(), c);
		auto iter_r = std::find(right.begin(), right.end(), c);

		if (iter_l != left.end())
		{
			score += iter_l - left.begin();
		}
		else if (iter_r != right.end())
		{
			score -= iter_r - right.begin();
		}
	}

	std::string winner = (score > 0 ? "Left" : "Right");

	return score == 0 ? "Let's fight again!" : winner + " side wins!";
}
