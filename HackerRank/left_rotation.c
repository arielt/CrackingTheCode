#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

/*
 * https://www.hackerrank.com/challenges/array-left-rotation
 */
int main(){
    int n;
    int k;
    scanf("%d %d",&n,&k);
    int ns = n * sizeof(int);
    int *a = malloc(ns);
    for(int a_i = 0; a_i < n; a_i++){
       scanf("%d",&a[a_i]);
    }

    int *b = malloc(ns);

    memcpy(b, a, ns);
    memcpy(a, b + k, (n-k) * sizeof(int));
    memcpy(a + n - k, b, k * sizeof(int));

    for(int a_i = 0; a_i < n; a_i++){
       printf("%d ",a[a_i]);
    }

    return 0;
}
