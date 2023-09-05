#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
struct listint_t {
    int data;
    struct listint_t *next;
};

typedef struct listint_t listint_t;

/* Function to check if a singly linked list has a cycle. */
int check_cycle(listint_t *list) {
    if (list == NULL || list->next == NULL) {
        return 0;  // No cycle in an empty list or a list with only one node.
    }

    listint_t *tortoise = list;  // Slow pointer (moves one step at a time).
    listint_t *hare = list;     // Fast pointer (moves two steps at a time).

    while (hare != NULL && hare->next != NULL) {
        tortoise = tortoise->next;   // Move the slow pointer one step.
        hare = hare->next->next;     // Move the fast pointer two steps.

        if (tortoise == hare) {
            return 1;  // The fast pointer caught up with the slow pointer; there is a cycle.
        }
    }

    return 0;  // No cycle found.
}

/* Example usage: */
int main() {
    listint_t *head = NULL;
    listint_t *second = NULL;
    listint_t *third = NULL;

    // Create a linked list with a cycle (1 -> 2 -> 3 -> 2).
    head = (listint_t *)malloc(sizeof(listint_t));
    second = (listint_t *)malloc(sizeof(listint_t));
    third = (listint_t *)malloc(sizeof(listint_t));

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = second;

    // Check if the linked list has a cycle.
    if (check_cycle(head)) {
        printf("The linked list has a cycle.\n");
    } else {
        printf("The linked list does not have a cycle.\n");
    }

    // Clean up the allocated memory.
    free(head);
    free(second);
    free(third);

    return 0;
}
