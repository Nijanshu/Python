#include<stdio.h>

// void f(int *p, int *q){
//     p=q;
//     *p=2;
// }

// int i=0, j=1;
void main(){

    int arr[]={1,4,8,12,16};

    int *a,*b;

    int i;
    a=arr;
    b=arr+2;
    i=*a+1;
    printf("%d %d %d",i,*a,*b);
    // char *ptr1= "Sale";
    // char *ptr1= "Sale";
    // int *ptr2= arr+5;
    // printf("%d\n", (*ptr2));
    // printf("%c\n", *ptr1+1);
    // int n;

    // int *ptr=arr+1;
    // int *ptr2=(int*)(&arr+1);

    // printf("%d\n", ptr);
    // printf("%d\n", ptr2);

    // unsigned int x[4][3]={{1,2,3},{4,5,6},{7,8,9},{10,11,12}};
    // printf("%u %u %u",*x+3,*(x+3),**(x+2)+3);


// f(&i,&j);
// printf("%d %d", i,j);

//     scanf("%d",&n);
//     int a=0, b=1;
    
// //     for(int i=0;i<n;i++){
// //         printf("%d ", a);
// //         int c=a+b;
// //         a=b;
// //         b=c;

}

//  for(int i=1; i<=n; i++){
     
//      for (int k = i-1; k<= (n+1)/2; k++){
//         printf(" ");
//      }
//         for (int j = 1; j<=i; j++)
//         {   
//             if(j==1 || j==i || i==n){

//                 printf("%d ", i);
//             }
//             else{
//                 printf("  ");
//             }

//         }
//         printf("\n");
//     }
// }