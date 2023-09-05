#ifndef CYCLE_CHECKER_H
#define CYCLE_CHECKER_H

/* Definition for singly-linked list. */
struct listint_t {
    int data;
    struct listint_t *next;
};

typedef struct listint_t listint_t;

/* Function to check if a singly linked list has a cycle. */
int check_cycle(listint_t *list);

#endif /* CYCLE_CHECKER_H */
