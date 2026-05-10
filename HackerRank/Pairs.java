import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/pairs
 */
public class Solution {
    static int pairs(int[] a,int k) {
        if (a.length == 1) return 0;
        int i = 0;
        int j = 1;
        int count = 0;
        int diff;
        Arrays.sort(a);
        while(true) {
            if (j > a.length-1) return count;
            diff = a[j] - a[i];
            if (diff == k) {
                count++;
                i++;
                j++;
            } else if (diff > k) {
                i++;
            } else {
                j++;
            }
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int res;

        String n = in.nextLine();
        String[] n_split = n.split(" ");

        int _a_size = Integer.parseInt(n_split[0]);
        int _k = Integer.parseInt(n_split[1]);

        int[] _a = new int[_a_size];
        int _a_item;
        String next = in.nextLine();
        String[] next_split = next.split(" ");

        for(int _a_i = 0; _a_i < _a_size; _a_i++) {
            _a_item = Integer.parseInt(next_split[_a_i]);
            _a[_a_i] = _a_item;
        }

        res = pairs(_a,_k);
        System.out.println(res);
    }
}
