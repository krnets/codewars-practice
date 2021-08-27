#pragma once

class Fighter
{
	std::string name;
	int health;
	int damagePerAttack;

public:
	Fighter(std::string name, int health, int damagePerAttack)
	{
		this->name = name;
		this->health = health;
		this->damagePerAttack = damagePerAttack;
	}

	~Fighter()
	{
	}

	std::string getName() { return name; }
	int getHealth() { return health; }
	int getDamagePerAttack() { return damagePerAttack; }
	void setHealth(int value) { health = value; }
};

/*
std::string declareWinner(Fighter* fighter1, Fighter* fighter2, std::string firstAttacker)
{
	auto attacker = firstAttacker == fighter1->getName() ? fighter1 : fighter2;
	auto opponent = firstAttacker != fighter1->getName() ? fighter1 : fighter2;

	while (attacker->getHealth() > 0 && opponent->getHealth() > 0)
	{
		opponent->setHealth(opponent->getHealth() - attacker->getDamagePerAttack());

		std::swap(opponent, attacker);
	}

	return attacker->getHealth() <= 0 ? opponent->getName() : attacker->getName();
}
*/

/*
std::string declareWinner(Fighter* fighter1, Fighter* fighter2, std::string firstAttacker)
{
	Fighter* attacker;
	Fighter* opponent;

	if (firstAttacker == fighter1->getName())
	{
		attacker = fighter1;
		opponent = fighter2;
	}
	else
	{
		attacker = fighter2;
		opponent = fighter1;
	}

	while (attacker->getHealth() > 0 && opponent->getHealth() > 0)
	{
		opponent->setHealth(opponent->getHealth() - attacker->getDamagePerAttack());

		std::swap(opponent, attacker);
	}

	return attacker->getHealth() <= 0 ? opponent->getName() : attacker->getName();
}
*/

std::string declareWinner(Fighter* fighter1, Fighter* fighter2, std::string firstAttacker)
{
	int f1_blows_survives = (fighter1->getHealth() - 1) / fighter2->getDamagePerAttack();
	int f2_blows_survives = (fighter2->getHealth() - 1) / fighter1->getDamagePerAttack();

	return f1_blows_survives == f2_blows_survives
		       ? firstAttacker
		       : f1_blows_survives > f2_blows_survives
		       ? fighter1->getName()
		       : fighter2->getName();
}
