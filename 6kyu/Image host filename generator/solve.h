#pragma once
#include <range/v3/all.hpp>

using std::string;

class nameManager
{
	std::vector<string> names_;
public:
	bool nameExists(const string& name);
	bool nameWasUnique(const string& name);
	string generateName();
};

inline bool nameManager::nameExists(const string& name)
{
	return ranges::any_of(names_, [&](auto& s) { return s == name; });
}

inline bool nameManager::nameWasUnique(const string& name)
{
	if (nameExists(name)) return false;

	names_.push_back(name);

	return true;
}


nameManager photoManager;

string generateName()
{
	srand(time(nullptr));
	string name;

	do
	{
		name = "";

		for (int i = 0; i < 6; ++i)
		{
			if (rand() & 1)
				name += rand() % 26 + 'A';
			else
				name += rand() % 26 + 'a';
		}
	}
	while (photoManager.nameExists(name));

	return name;
}
