#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int elements[2048];
	int i, size;

	if (!*head || !(*head)->next)
		return (1);

	current = *head;
	size = 0;
	while (current)
	{
		elements[size] = current->n;
		size++;
		current = current->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (elements[i] != elements[size - i - 1])
			return (0);
	}

	return (1);
}
