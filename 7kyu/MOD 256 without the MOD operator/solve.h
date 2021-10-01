#pragma once

/*
int mod256WithoutMod(int number)
{
	return number - (number / 256 * 256);
}
*/

/*int mod256WithoutMod(int number)
{
	return number < 0 ? -mod256WithoutMod(-number) : number & 0xFF;
}*/

/*
int mod256WithoutMod(int number)
{
	return number < 0 ? -(-number & 255) : number & 255;
}
*/

int mod256WithoutMod(int number)
{
	return number < 0 ? -(-number & 0xFF) : number & 0xFF;
}
