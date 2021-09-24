#pragma once

#include <string>

class Node
{
public:
	int data;
	Node* next;

	Node(int data, Node* next = nullptr)
	{
		this->data = data;
		this->next = next;
	}
};

/*
std::string stringify(Node* list)
{
	std::string s;
	Node* current = list;

	while (current != nullptr)
	{
		s += std::to_string(current->data);
		s += " -> ";

		current = current->next;
	}

	return s + "nullptr";
}
*/

/*
std::string stringify(Node* list)
{
	std::ostringstream oss;

	while (list)
	{
		oss << list->data << " -> ";
		list = list->next;
	}
	oss << "nullptr";

	return oss.str();
}
*/

std::string stringify(Node* list)
{
	return list ? std::to_string(list->data) + " -> " + stringify(list->next) : "nullptr";
}
