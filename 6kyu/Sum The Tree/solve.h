#pragma once

struct node
{
	int value;
	node* left;
	node* right;
};

int sumTheTreeValues(node* root)
{
	if (!root) return 0;

	int sumLeft = sumTheTreeValues(root->left);
	int sumRight = sumTheTreeValues(root->right);

	return sumLeft + root->value + sumRight;
}
