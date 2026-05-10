import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/common-child
 */
public class Solution {

    /*
     * Longest common substring
     */
    public static int lcs(char[] s1, char[] s2) {
        int[][] memo = new int[s1.length + 1][s2.length + 1];

        for (int i=0; i <= s1.length; i++) {
            for (int j=0; j <= s2.length; j++) {
                if (i == 0 || j == 0) {
                    memo[i][j] = 0;
                }
                else if (s1[i-1] == s2[j-1]) {
                    memo[i][j] = 1 + memo[i-1][j-1];
                } else {
                    memo[i][j] = Math.max(memo[i-1][j], memo[i][j-1]);
                }
            }
        }
        return memo[s1.length][s2.length];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(lcs(sc.next().toCharArray(), sc.next().toCharArray()));
    }
}
