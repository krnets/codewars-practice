bool amIWilson(unsigned n)
{
	unsigned modulus = n * n;
	unsigned product = 1;

	for (unsigned factor = 2; factor < n; ++factor)
	{
		product = (product * factor) % modulus;
	}

	return product + 1 == modulus;
}
