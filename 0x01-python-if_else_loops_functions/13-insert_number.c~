#include "lists.h"

// Define the structure for a singly linked list node
struct listint_t {
    int data;
    struct listint_t* next;
};

// Define a type alias for convenience
typedef struct listint_t listint_t;

// Function to insert a number into a sorted singly linked list
listint_t* insert_node(listint_t** head, int number) {
    // Create a new node
    listint_t* new_node = (listint_t*)malloc(sizeof(listint_t));
    if (new_node == NULL) {
        // Memory allocation failed
        return NULL;
    }

    new_node->data = number;
    new_node->next = NULL;

    // If the list is empty or the new node should be inserted at the beginning
    if (*head == NULL || number < (*head)->data) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    // Traverse the list to find the insertion point
    listint_t* current = *head;
    while (current->next != NULL && current->next->data < number) {
        current = current->next;
    }

    // Insert the new node after 'current'
    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}

// Function to print the linked list
void print_list(listint_t* head) {
    listint_t* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Function to free the memory allocated for the linked list
void free_list(listint_t* head) {
    while (head != NULL) {
        listint_t* temp = head;
        head = head->next;
        free(temp);
    }
}

int main() {
    listint_t* head = NULL;

    // Insert elements into the sorted linked list
    insert_node(&head, 5);
    insert_node(&head, 3);
    insert_node(&head, 8);
    insert_node(&head, 1);

    // Print the linked list
    printf("Linked List: ");
    print_list(head);

    // Free the memory allocated for the linked list
    free_list(head);

    return 0;
}
