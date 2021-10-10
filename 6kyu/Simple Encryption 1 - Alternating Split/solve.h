#pragma once

using std::string;

string encrypt(string text, int n)
{
	if (n <= 0) return text;

	while (n > 0)
	{
		string even, odd;

		for (int i = 0; i < text.length(); ++i)
		{
			if (i % 2 == 0)
				even += text[i];
			else odd += text[i];
		}
		text = odd + even;
		--n;
	}
	return text;
}

string decrypt(string encryptedText, int n)
{
	if (n <= 0) return encryptedText;

	while (n > 0)
	{
		int mid = encryptedText.length() / 2;
		auto left = encryptedText.begin();
		auto right = encryptedText.begin() + mid;
		string decrypted;

		for (int i = 0; i < encryptedText.length(); ++i)
		{
			if (i % 2 == 0)
				decrypted += *right++;
			else
				decrypted += *left++;
		}
		encryptedText = decrypted;
		--n;
	}
	return encryptedText;
}
