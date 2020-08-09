#include <stdio.h>
#define SIZE 5

struct Queue
{
	int places[SIZE];
	int front;
	int rear;
};

int enqueue(struct Queue *queue, int value)
{
	if(queue -> rear == SIZE-1)
	{
		printf("The queue is full.\n");
		return 1;
	}
	else
	{
		if(queue -> front == -1)
			queue -> front = 0;
		queue -> rear++;
		queue -> places[queue -> rear] = value;
		printf("%d added to queue.\n", value);
		return 0;
	}
};

int dequeue(struct Queue *queue)
{
	if(queue -> front == -1)
	{
		printf("The queue is empty.\n");
		return 1;
	}
	else
	{
		int value = queue -> places[queue -> front];
		printf("%d is removed from the queue.\n", value);
		queue -> front++;
		if(queue -> front > queue -> rear)
		{
			queue -> front = queue -> rear = -1;
			printf("The queue is empty.\n");
		}
		return 0;
	}
};

int main(int argc, char const *argv[])
{
	struct Queue queue = { .front = -1, .rear=-1 };
	for (int i = 1; i <= 6; i++)
		enqueue(&queue, i);
	for (int i = 1; i <= 6; i++)
		dequeue(&queue);
}
