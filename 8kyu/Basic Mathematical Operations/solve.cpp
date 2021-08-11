int basicOp(char op, int val1, int val2)
{
	int ans = 0;

	switch (op)
	{
	case '+': ans = val1 + val2;
		break;
	case '-': ans = val1 - val2;
		break;
	case '*': ans = val1 * val2;
		break;
	case '/': ans = val1 / val2;
		break;
	default: ;
	}

	return ans;
}
