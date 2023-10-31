#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp;

	temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (temp->n >= number || temp == NULL)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
