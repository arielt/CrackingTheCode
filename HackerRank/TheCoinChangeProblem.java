import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/coin-change
 */

public class Solution {

    private static long coins(int N, int M, int[] C) {
        long t[][] = new long[M+1][N+1];

        for (int j=0; j < N+1; j++) {
            for (int i=0; i < M+1; i++) {
                if(i==0 || j==0) {
                    t[i][j] = 0;
                } else {
                    int rem = j - C[i-1];
                    // +1 if remnant is 0
                    if (rem == 0)
                        t[i][j] = 1;
                    // upper element
                    t[i][j] += t[i-1][j];
                    // left element
                    if (rem > 0)
                        t[i][j] += t[i][rem];
                }
            }
        }

        return t[M][N];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int arr[] = new int[M];
        for(int i=0; i < M; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(coins(N, M, arr));
    }
}
