#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *head2 = NULL;

	copy_list(&head2, head);

	reverse_list(&head2);

	return compare(head, &head2);
}

int copy_list(listint_t **dest, listint_t **src)
{

	const listint_t *current;
	current = *src;

	while ((current) != NULL)
	{
		add_nodeint_end(dest, current->n);
		current = current->next;
	}
}
int reverse_list(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *prev = NULL;

	while (curr != NULL)
	{
		listint_t *next = curr->next;
		curr->next = prev;

		/*update previous*/
		prev = curr;

		/*increment */
		curr = next;
	}

	*head = prev;
	return 0;
}

int compare(listint_t **head1, listint_t **head2)
{
	listint_t *curr1 = *head1;
	listint_t *curr2 = *head2;

	while (curr1 != NULL && curr2 != NULL)
	{
		if (curr1->n != curr2->n)
			return 0;

		curr1 = curr1->next;
		curr2 = curr2->next;
	}
	return 1;
}