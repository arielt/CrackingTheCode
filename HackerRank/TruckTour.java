import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/truck-tour
 */
public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();

        long[] reserve = new long[n];
        int i;

        for (i = 0; i<n; i++) {
            reserve[i] = sc.nextLong() - sc.nextLong();
        }

        int start = 0;
        long sum = 0;
        int length = 0;
        i = 0;

        while(true) {
            sum += reserve[i];
            length++;
            if (length == n){
                System.out.println(start);
                return;
            }

            // loop
            if (i == n-1) {
                i=0;
            } else {
                i++;
            }

            // start over
            if (sum < 0) {
                start = i;
                sum = 0;
                length = 0;
            }
        }
    }
}
