

std::string bumps(std::string road)
{
	return std::count(road.begin(), road.end(), 'n') <= 15 ? "Woohoo!" : "Car Dead";
}
