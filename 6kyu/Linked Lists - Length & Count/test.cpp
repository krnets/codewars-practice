#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("Node length and count tests")
{
	SUBCASE("testing tests_for_counting_the_length_of_a_linked_list")
	{
		Node* head = new Node;
		Node* n = head;
		for (int i = 0; i < 10; ++i)
		{
			n->next = new Node(i);
			n = n->next;
		}
		CHECK(Length(nullptr) == 0);
		CHECK(Length(new Node(65)) == 1);
		CHECK(Length(head) == 11);
	}
	SUBCASE("tests_for_counting_occurrences_of_a_particular_integer_in_a_linked_list")
	{
		Node* head = new Node;
		Node* n = head;
		for (int i = 0; i < 11; ++i)
		{
			n->next = new Node(i / 2);
			n = n->next;
		}
		CHECK(Count(nullptr, 0) == 0);
		CHECK(Count(new Node, 0) == 1);
		CHECK(Count(new Node, 5) == 0);
		CHECK(Count(head, 0) == 3);
		CHECK(Count(head, 4) == 2);
		CHECK(Count(head, 5) == 1);
	}
	SUBCASE("random_tests")
	{
		int size = 10000;
		Node* head = new Node;
		Node* n = head;
		int count_five = 0;
		int count_ninetyseven = 0;
		for (int i = 1; i < size; ++i)
		{
			n->next = new Node(rand() % 300);
			n = n->next;
			if (n->data == 5)
				++count_five;
			else if (n->data == 97)
				++count_ninetyseven;
		}

		CHECK(Length(head) == size);
		CHECK(Count(head, 5) == count_five);
		CHECK(Count(head, 97) == count_ninetyseven);
		CHECK(Count(head, 500) == 0);
	}
}
