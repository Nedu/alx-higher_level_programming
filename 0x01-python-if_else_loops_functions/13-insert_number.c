#include "lists.h"

/**
 * insert_node - Insert in sorted linked list
 *
 * @head: list head
 * @number: number to store in the new node
 * 
 * Author: Nedu Robert
 * Return: pointer to new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *newNode;

	temp = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (*head == NULL || (*head)->n > number)
	{
			newNode->next = *head;
			*head = newNode;
			return (newNode);
	}

	while (temp->next != NULL)
	{
			if ((temp->next)->n >= number)
			{
					newNode->next = temp->next;
					temp->next = newNode;
					return (newNode);
			}
			temp = temp->next;
	}

	newNode->next = NULL;
	temp->next = newNode;
	return (newNode);
}
