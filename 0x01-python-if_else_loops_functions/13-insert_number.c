#include "lists.h"

/**
* insert_node - as the name suggests ?? xD
* @head: pointer to the head of the list
* @number: the number
* Return: adress of the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *ptr, *new, *previous;

    /* creation of the node*/
    new = malloc(sizeof(listint_t));
    if (new == NULL)
    {
        free(new);
        return (NULL);
    }
    new->n = number;
    new->next = NULL;
    if (head == NULL || *head == NULL)
    {
        *head = new;
        return (new);  
    }
    ptr = *head;
    if (ptr->n >= number)
        {
            new->next = ptr;
            *head = new;
            return (new);
        } 
    previous = ptr;
    ptr = ptr->next;
    while (ptr != NULL)
    {
        if (number <= ptr->n)
        {
            previous->next = new;
            new->next = ptr;
            return (new);
        }
        previous = ptr;
        ptr = ptr->next;
    }
    previous->next = new;
    return (new);
}
