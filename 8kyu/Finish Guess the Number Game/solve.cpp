#include <stdexcept>

class Guesser
{
public:
	Guesser(int number, int lives) : number(number), lives(lives)
	{
	}

	bool guess(int n)
	{
		if (lives <= 0)
			throw std::runtime_error("ran out of lives");

		if (n != number)
			--lives;

		return n == number;
	}

private:
	int number, lives;
};
