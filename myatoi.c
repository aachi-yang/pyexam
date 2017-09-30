#include <stdio.h>
#include <limits.h>

int main(int argc, char *argv[])
{   
    printf("Hello, World!\n");
    char *a = "++1";
    char *b = "--1";
    char *c = "+1234";
    char *d = "-1234";
    char *e = "-  1234";
    char *f = "-1234a24";
    char *g = "-12-34a24";
    char *h = "    -12-34a24";
    char *i = " 2147483647";
    char *j = "-2147483648";
    char *k = "-1";
    
    printf("a = %d\n", atoi(a));
    printf("b = %d\n", atoi(b));
    printf("c = %d\n", atoi(c));
    printf("d = %d\n", atoi(d));
    printf("e = %d\n", atoi(e));
    printf("f = %d\n", atoi(f));
    printf("g = %d\n", atoi(g));
    printf("h = %d\n", atoi(h));
    printf("i = %x\n", atoi(i));
    printf("j = %x\n", atoi(j));
    printf("k = %x\n", atoi(k));

    
    printf("min %d max %d\n", INT_MAX, INT_MIN);

    return 0;
}