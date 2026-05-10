import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/array-left-rotation
 */
public class Solution {

    private static void shift(int a[], int n) {
        int s = a[0];
        int i;
        for (i=0; i<n-1; i++) {
            a[i] = a[i+1];
        }
        a[i] = s;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }

        int i;

        for(i=0;i<k;i++) {
            shift(a,n);
        }

        for (i=0;i<n;i++) {
          System.out.print(a[i]);
          System.out.print(" ");
        }
    }
}
