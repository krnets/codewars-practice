#include <string>
#include <vector>

/*
std::string get_planet_name(int id)
{
	std::vector<std::string> planets{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};

	return planets.at(id - 1);
}
*/

std::string get_planet_name(int id)
{
	std::string planets[] = {"", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};

	return planets[id];
}
