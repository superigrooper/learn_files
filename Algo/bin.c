#include <stdio.h>

#define LENGTH 10

int bin_search(int list[], int item, int length);

int main(void)
{
    int list[LENGTH] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int item = 59;
    printf("%i\n", bin_search(list, item, LENGTH));
}

int bin_search(int list[], int item, int length)
{
    int low = 0;
    int high = length - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        int guess = list[mid];
        
        if (guess == item)
        {
            return mid;
        }
        if (guess > item)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }       
    }
    return -1;
}