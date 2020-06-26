#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BASE 1024
int* twoSum(int* nums, int target);


int main(){
    int num_list[] = {3,22,2,2,3};
    int target = 6;

    int* finalArray = twoSum(num_list, target);
    printf("First: %i\nSecond: %i\n", finalArray[0], finalArray[1]);
    free(finalArray);
    return 0;
}

int* twoSum(int* nums, int target){
    int numsSize = sizeof(nums);
    int returnSize = 2;
    int *returnArray = (int*)malloc(returnSize * sizeof(int*));
    int temp = 0;
    for (int i = 0; i<numsSize; i++){
        temp = i;
        for (int j = temp+1; j<numsSize;j++){
            if (nums[temp] + nums[j] == target){
                returnArray[0] = temp;
                returnArray[1] = j;
                return(returnArray);
            }
        }
    }   
    return(NULL);
}

