import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/maxsubarray
 */
public class Solution {

    public static int maxSubArray(int arr[]) {
        int maxNonNegative = arr[0];
        int sum = 0;

        for (int i=0; i < arr.length; i++) {
            if (arr[i] > 0)
                sum += arr[i];
            else if (arr[i] > maxNonNegative)
                maxNonNegative = arr[i];
        }

        if (sum > 0)
            return sum;
        else
            return maxNonNegative;
    }

    public static int maxContSubArray(int arr[]) {
        int maxNonNegative = arr[0];
        int sum = 0;
        int maxSum = arr[0];

        for (int i=0; i < arr.length; i++) {
            sum += arr[i];

            if (arr[i] > maxNonNegative)
                maxNonNegative = arr[i];

            if (sum > maxSum)
                maxSum = sum;

            if (sum < 0) {
                sum = 0;
            }
        }

        if (sum > 0)
            return maxSum;
        else
            return maxNonNegative;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int cases = sc.nextInt();

        for (int i=0; i<cases; i++) {
            int n = sc.nextInt();
            int arr[] = new int[n];
            for (int j=0; j<n; j++) {
                arr[j] = sc.nextInt();
            }
            System.out.println(maxContSubArray(arr) + " " + maxSubArray(arr));
        }
    }
}
