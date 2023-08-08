#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: head of linked list
 * @number: index to insert
 * Return: the address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *h;
	int num;

	h = malloc(sizeof(listint_t));
	h->n = number;
	h->next = NULL;
	num = number;

	if (*head == NULL || num < (*head)->n)
	{
		h->next = *head;
		*head = h;
	}
	else
	{
		tmp = *head;
		while (tmp->next != NULL && tmp->next->n < num)
			tmp = tmp->next;
		h->next = tmp->next;
		tmp->next = h;
	}
	return (*head);
}
