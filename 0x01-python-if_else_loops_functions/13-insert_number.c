#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* insert_node - inserts a number into a sorted singly linked list
* @head: pointer to pointer of the first node of the list
* @number: the integer to be inserted
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *newNode = malloc(sizeof(listint_t));
listint_t *current = *head;
listint_t *previous = NULL;

if (newNode == NULL)
return (NULL);

newNode->n = number;
newNode->next = NULL;

if (*head == NULL || number < current->n)
{
newNode->next = *head;
*head = newNode;
return (newNode);
}

while (current && number >= current->n)
{
previous = current;
current = current->next;
}

previous->next = newNode;
newNode->next = current;

return (newNode);
}
