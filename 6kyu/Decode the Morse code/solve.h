#pragma once

#include <regex>
#include <unordered_map>

using std::string;

std::unordered_map<string, string> MORSE_CODE{
	{".-", "A"},
	{"-...", "B"},
	{"-.-.", "C"},
	{"-..", "D"},
	{".", "E"},
	{"..-.", "F"},
	{"--.", "G"},
	{"....", "H"},
	{"..", "I"},
	{".---", "J"},
	{"-.-", "K"},
	{".-..", "L"},
	{"--", "M"},
	{"-.", "N"},
	{"---", "O"},
	{".--.", "P"},
	{"--.-", "Q"},
	{".-.", "R"},
	{"...", "S"},
	{"-", "T"},
	{"..-", "U"},
	{"...-", "V"},
	{".--", "W"},
	{"-..-", "X"},
	{"-.--", "Y"},
	{"--..", "Z"},
	{"-----", "0"},
	{".----", "1"},
	{"..---", "2"},
	{"...--", "3"},
	{"....-", "4"},
	{".....", "5"},
	{"-....", "6"},
	{"--...", "7"},
	{"---..", "8"},
	{"----.", "9"},
	{".-.-.-", "."},
	{"--..--", ","},
	{"..--..", "?"},
	{".----.", "'"},
	{"-.-.--", "!"},
	{"-..-.", "/"},
	{"-.--.", "("},
	{"-.--.-", ")"},
	{".-...", "&"},
	{"---...", "=>"},
	{"-.-.-.", ";"},
	{"-...-", "="},
	{".-.-.", "+"},
	{"-....-", "-"},
	{"..--.-", "_"},
	{".-..-.", "\""},
	{"...-..-", "$"},
	{".--.-.", "@"},
	{"...---...", "SOS"}
};


string decodeMorse(string morseCode)
{
	string decoded, morse;
	std::regex re("\\s{3}");
	auto left = morseCode.find_first_not_of(' ');
	auto right = morseCode.find_last_not_of(' ') + 1;
	auto it = std::sregex_token_iterator(morseCode.begin() + left, morseCode.begin() + right, re, -1);

	for_each(it, {}, [&](auto m)
	{
		std::istringstream iss(m.str());

		while (iss >> morse)
			decoded.append(MORSE_CODE[morse]);

		decoded += ' ';
	});
	decoded.pop_back();

	return decoded;
}
