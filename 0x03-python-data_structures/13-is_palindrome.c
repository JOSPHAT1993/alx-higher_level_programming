#include "lists.h"
/**
 * palidrome-main function to check for palidrome
 *
 * @left:'head of singly list'
 * @right:'tail of a singly list'
 *
 * Return:0 if not palidrom, 1 if it is
 */
int palidrome(listint_t **left, listint_t right)
{
	int is_palidrome;

	if (right == NULL)
	{
		return (1);
	}

	is_palidrome = (palidrome(left, right->next) && (*left)->n == right->n);
	*left = (*left)->next;

	return (is_palidrome);
}

/**
 * is_paledrome-function to check for palidrome
 *
 * @head:'singly list head'
 *
 * Return:0 if not palidrom, 1 if palidrome
 */
int is_paledrome(listint_t **head)
{
	if (!(*head) || !head)
		return (1);

	return (palidrome(head, *head));
}
