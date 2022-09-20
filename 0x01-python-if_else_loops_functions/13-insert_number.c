#include "lists.h"
#include <stdlib.h>
/**
 * insert_node-inserting value at nth position
 *
 * @head:'head of linked lists variable'
 * @number:'Integer variable for position'
 *
 * Return:address of the added node if success, else fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new = *head;

	temp = malloc(sizeof(listint_t));

	if (temp == NULL)
	{
		return (0);
	}

	temp->n = number;
	if (*head == 0 || new->n >= number)
	{
		temp->next = new;
		*head = temp;
		return (temp);
	}
	while (new->next && new->next->n <= number)
	{
		new = new->next;
	}
	temp->next = new->next;
	new->next = temp;
	return (temp);
}
