#include "lists.h"

/**
* check_cycle - check for cycle in single linked list
* @list: head of the list
* Return: 0 if none 1 otherwise
*/

int check_cycle(listint_t *list)
{
	int i, n = 1;
	listint_t *ptrtest, *next;

	if (list == NULL)
		return (0);
	ptrtest = list->next;
	while (ptrtest != NULL)
	{
		next = list;
		i = 0;
		while (next != NULL && i < n)
		{
		if (next == ptrtest)
		return (1);
		next = next->next;
		i++;
		}
		ptrtest = ptrtest->next;
		n++;
	}
	return (0);
}
