import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/jesse-and-cookies
 */
public class Solution {

    public static void main(String[] args) {
        Integer first, second;
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int count = 0;

        PriorityQueue<Integer> cookies = new PriorityQueue<Integer>();
        for (int i=0; i<n; i++) {
            cookies.add(sc.nextInt());
        }

        while(true) {
            if (cookies.peek() >= k) {
                System.out.println(count);
                return;
            }

            if (cookies.size() > 1) {
              cookies.add(cookies.remove() + 2*cookies.remove());
              count++;
            } else {
                break;
            }
        }
        System.out.println("-1");
    }
}
