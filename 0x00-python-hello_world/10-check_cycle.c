#include "lists.h"

int check_cycle(listint_t *list)
{
	int i, n = 1;
	listint_t *ptrtest, *next;

	if (list != NULL)
	{
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
}
return (0);
}
