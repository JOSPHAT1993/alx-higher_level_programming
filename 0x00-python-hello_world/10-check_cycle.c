#include "lists.h"
/**
 * check_cycle-main function to check cycles in singly li
 *
 * @list:'Linked list elements'
 *
 * Return:0 if no cycle, 1 if a cycle exist
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *temp = list;

	while (temp && temp->next)
	{
		current = current->next;
		temp = temp->next->next;
		if (current == temp)
			return (1);
	}
	return (0);
}
