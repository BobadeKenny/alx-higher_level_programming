#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
    const listint_t *current;
    const listint_t *tail;
    unsigned int n = 0;

    while (head != NULL)
    {
        current = head;
        head = head->next;
    }
    while (head != NULL)
    {
        current = head;
        head = head->next;
    }
    return(n);
}
