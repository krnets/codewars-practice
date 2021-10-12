#pragma once

struct Node
{
	Node* next;
	int data;

	Node() : next(nullptr), data(0) { }
	Node(int d) : next(nullptr), data(d) { }
	Node(Node* n, int d) : next(n), data(d) { }
};

/*
int Length(Node* head)
{
	return !head ? 0 : 1 + Length(head->next);
}

int Count(Node* head, int data)
{
	return !head ? 0 : (head->data == data) + Count(head->next, data);
}
*/

int Length(Node* head)
{
	if (!head) return 0;

	int len = 0;

	while (head)
	{
		++len;
		head = head->next;
	}

	return len;
}

int Count(Node* head, int data)
{
	if (!head) return 0;

	int cnt = 0;

	while (head)
	{
		if (head->data == data)
			++cnt;

		head = head->next;
	}
	return cnt;
}

