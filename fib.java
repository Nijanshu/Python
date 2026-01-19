import java.util.Scanner;

public class fib{

    public static void main(String[] args){

        int n;
        Scanner sc = new Scanner(System.in);
        n= sc.nextInt();
        
        // int a=0, b=1;
       
//        for(int i=0;i<n;i++){
//            System.out.print(a +" ");
//            int c=a+b;
//            a=b;
//            b=c;
//    }

        for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            System.out.print("* ");
        }
        System.out.println();
    }
    }
}