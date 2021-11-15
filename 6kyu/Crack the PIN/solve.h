#pragma once

#include <iomanip>
#include <fmt/core.h>
#include <openssl/md5.h>

using std::string;

string crack(const string& hash)
{
	unsigned char md[MD5_DIGEST_LENGTH];

	for (int pin = 0; pin < 100'000; ++pin)
	{
		string pin_str = fmt::format("{:05}", pin);

		MD5((unsigned char*)pin_str.c_str(), 5, md);

		std::ostringstream oss;
		oss << std::hex << std::setfill('0');

		for (long long c : md)
			oss << std::setw(2) << c;

		if (oss.str() == hash)
			return pin_str;
	}

	return string();
}
