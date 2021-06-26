// linkedlist.cpp

#include <iostream>

using namespace std;

struct node {
   int data;
   struct node *next;
};

void insert(struct node **head, int data) {
   struct node *n = (struct node*) malloc(sizeof(struct node));
   n->data = data;
   n->next = *head;
   *head = n;
}

// One asterisk means pointer to the type of the var...
// Two asterisks means pointer to a pointer to the type of the var...
void reverse(struct node **head) {
   struct node *prev = NULL;
   struct node *curr = *head;
   struct node *next;
   while (curr != NULL) {
      next = curr->next;

      curr->next = prev;
      prev = curr;

      curr = next;
   }
   *head = prev;
}

void printList(struct node *head) {
   struct node *temp = head;
   while (temp != NULL) {
      cout << temp->data << " -> ";
      temp = temp->next;
   }
   cout << endl;
}

int main(int argc, char *argv[])
{
   struct node *head = NULL;

   insert(&head, 1);
   insert(&head, 2);
   insert(&head, 3);
   insert(&head, 4);
   insert(&head, 5);

   cout << " ---- Linked List 4 ----" << endl;

   printList(head);
}