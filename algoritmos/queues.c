#include <stdio.h>
#define SIZE 5

struct Queue
{
	int places[SIZE];
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
		queue -> rear++;
		queue -> places[queue -> rear] = value;
		printf("%d added to queue.\n", value);
		return 0;
	}
};

int dequeue(struct Queue *queue)
{
	if(queue -> rear == -1)
	{
		printf("The queue is empty.\n");
		return 1;
	}
	else
	{
		int value = queue -> places[0];
		printf("%d is removed from the queue.\n", value);
		for (int i = 0; i < queue -> rear; i ++)
			queue -> places[i] = queue -> places[i+1];
		queue -> rear--;
		if(queue -> rear == -1)
		{
			printf("The queue is empty.\n");
		}
		return 0;
	}
};

int main(int argc, char const *argv[])
{
	struct Queue queue = { .rear=-1 };
	for (int i = 1; i <= 6; i++)
		enqueue(&queue, i);
	for (int i = 1; i <= 6; i++)
		dequeue(&queue);
}
