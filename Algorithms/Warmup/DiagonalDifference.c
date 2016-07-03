#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n, d1 = 0, d2 = 0, tot;
    scanf("%d",&n);
    int i, j, A[n][n];
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
            scanf("%d",&A[i][j]);
    for(i = 0; i < n; i++) {
        d1 += A[i][i];
        d2 += A[i][n-1-i];
    }
    tot = d1 - d2;
    if(tot >= 0)
        printf("%d",tot);
    else
        printf("%d",-1*tot);
    return 0;
}
