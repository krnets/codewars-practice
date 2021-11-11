#pragma once

#include <cstring>

char* sortTheInnerContent(const char* words, int length)
{
	char* dst = new char[length + 1];
	memcpy(dst, words, length);
	dst[length] = '\0';

	int L = 0;

	while (L != length)
	{
		while (L < length && dst[L] == ' ') ++L;

		int R = L;

		while (R < length && dst[R] != ' ') ++R;

		if (R - L > 2)
			sort(dst + L + 1, dst + R - 1, std::greater());

		L = R;
	}

	return dst;
}
