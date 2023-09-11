#include "lists.h"
int is_palindrome(listint_t **head)
{
	int len = list_len(*head);
	printf("-----------------------------\n");
	listint_t *x = half_list(*head, len);

	reverse_list(&x);
	print_listint(*head);
}

listint_t *half_list(listint_t *head, int len)
{

	listint_t *curr = head;
	int index = 0;
	int is_odd = len % 2 == 0;
	while (curr)
	{
		if (index == (len / 2))
		{
			if (is_odd == 1)
				return curr->next;

			return curr;
		}

		curr = curr->next;
		index++;
	}
	return NULL;
}

int reverse_list(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *prev = *head;

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

int list_len(listint_t *head)
{
	int len = 0;
	listint_t *curr = head;
	while (curr)
	{
		len++;
		curr = curr->next;
	}
	return len;
}
