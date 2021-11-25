#pragma once

using std::string;

string catMouse(string field, unsigned int jump)
{
	int mouse_pos = -1, cat_pos = -1, dog_pos = -1;

	for (int i = 0; i < field.length(); ++i)
	{
		switch (field[i])
		{
		case 'C': cat_pos = i; break;
		case 'D': dog_pos = i; break;
		case 'm': mouse_pos = i; break;
		}
	}
	if (mouse_pos < 0 || cat_pos < 0 || dog_pos < 0)
		return "boring without all three";

	if (abs(mouse_pos - cat_pos) > jump)
		return "Escaped!";

	if ((cat_pos < dog_pos && dog_pos < mouse_pos) ||
		(mouse_pos < dog_pos && dog_pos < cat_pos))
		return "Protected!";

	return "Caught!";
}
