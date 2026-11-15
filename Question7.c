/* Functions to perform front insertion, rear insertion, front deletion, and rear deletion on a double ended queue*/
#include <stdio.h>
#define MAX 10

int deque[MAX];
int front = -1;
int rear = -1;

int isFull() {
    return ((front == 0 && rear == MAX - 1) || (front == rear + 1));
}

int isEmpty() {
    return (front == -1);
}

// a. Front Insertion
void insertFront(int item) {
    if (isFull()) {
        printf("Deque Overflow: Cannot insert at front.\n");
        return;
    }
    if (isEmpty()) {
        front = 0;
        rear = 0;
    } else if (front == 0) {
        front = MAX - 1;
    } else {
        front = front - 1;
    }
    deque[front] = item;
    printf("Inserted %d at front.\n", item);
}

// b. Rear Insertion
void insertRear(int item) {
    if (isFull()) {
        printf("Deque Overflow: Cannot insert at rear.\n");
        return;
    }
    if (isEmpty()) {
        front = 0;
        rear = 0;
    } else if (rear == MAX - 1) {
        rear = 0;
    } else {
        rear = rear + 1;
    }
    deque[rear] = item;
    printf("Inserted %d at rear.\n", item);
}

// c. Front Deletion
int deleteFront() {
    if (isEmpty()) {
        printf("Deque Underflow: Cannot delete from front.\n");
        return -1;
    }
    int deleted = deque[front];
    if (front == rear) {
        front = -1;
        rear = -1;
    } else if (front == MAX - 1) {
        front = 0;
    } else {
        front = front + 1;
    }
    return deleted;
}

// d. Rear Deletion
int deleteRear() {
    if (isEmpty()) {
        printf("Deque Underflow: Cannot delete from rear.\n");
        return -1;
    }
    int deleted = deque[rear];
    if (front == rear) {
        front = -1;
        rear = -1;
    } else if (rear == 0) {
        rear = MAX - 1;
    } else {
        rear = rear - 1;
    }
    return deleted;
}

// Helper function to display current deque state
void display() {
    if (isEmpty()) {
        printf("Deque is empty.\n");
        return;
    }
    printf("Current Deque: ");
    int i = front;
    while (1) {
        printf("%d ", deque[i]);
        if (i == rear)
            break;
        i = (i + 1) % MAX;
    }
    printf("\n");
}

int main() {
    insertRear(10);
    insertRear(20);
    insertFront(5);
    insertFront(2);
    display(); // Expected: 2 5 10 20

    printf("Deleted from front: %d\n", deleteFront()); // Removes 2
    printf("Deleted from rear: %d\n", deleteRear());   // Removes 20
    display(); // Expected: 5 10

    return 0;
}