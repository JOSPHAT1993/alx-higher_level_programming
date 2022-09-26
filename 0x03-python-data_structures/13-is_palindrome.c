#include "lists.h"
/**
 * palindrome-main function to check for palidrome
 *
 * @left:'head of singly list'
 * @right:'tail of a singly list'
 *
 * Return:0 if not palidrom, 1 if it is
 */
int palindrome(listint_t **left, listint_t right)
{
	int isPalidrome;

	if (right == NULL)
	{
		return (1);
	}

	isPalidrome = (palidrome(left, right->next) && (*left)->n == right->n);
	*left = (*left)->next;

	return (isPalidrome);
}

/**
 * is_palindrome-function to check for palidrome
 *
 * @head:'singly list head'
 *
 * Return:0 if not palidrom, 1 if palidrome
 */
int is_palindrome(listint_t **head)
{
	if (!(*head) || !head)
		return (1);

	return (palidrome(head, *head));
}
