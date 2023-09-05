#ifndef SORTED_LINKED_LIST_H
#define SORTED_LINKED_LIST_H

// Define the structure for a singly linked list node
struct listint_t {
    int data;
    struct listint_t* next;
};

// Define a type alias for convenience
typedef struct listint_t listint_t;

/**
 * Inserts a number into a sorted singly linked list.
 * @param head The pointer to the head of the list.
 * @param number The number to be inserted.
 * @return The address of the new node, or NULL if it fails.
 */
listint_t* insert_node(listint_t** head, int number);

/**
 * Prints the elements of the linked list.
 * @param head The pointer to the head of the list.
 */
void print_list(listint_t* head);

/**
 * Frees the memory allocated for the linked list.
 * @param head The pointer to the head of the list.
 */
void free_list(listint_t* head);

#endif /* SORTED_LINKED_LIST_H */
