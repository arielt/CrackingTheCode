import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/find-the-median
 */
public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        PriorityQueue<Integer> minHeap=new PriorityQueue();

        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        int q;
        Integer l,r;

        PriorityQueue maxHeap=new PriorityQueue<Integer>(n, Collections.reverseOrder());

        maxHeap.add(Integer.MIN_VALUE);
        minHeap.add(Integer.MAX_VALUE);

        for(int i=0; i<n; i++) {
            q = sc.nextInt();
            l = (Integer)maxHeap.peek();
            r = (Integer)minHeap.peek();
            //System.out.println("values:" + q + l + r);

            // insert new value
                if (q < r) {
                    maxHeap.add(q);
                } else {
                    minHeap.add(q);
                }

            // rebalance
            if ((maxHeap.size() - minHeap.size()) > 1) {
                minHeap.add((Integer)maxHeap.remove());
            } else if ((minHeap.size() - maxHeap.size()) > 1) {
                maxHeap.add((Integer)minHeap.remove());
            }

            if (maxHeap.size() > minHeap.size()) {
                System.out.println((float)(Integer)maxHeap.peek());
            } else if (maxHeap.size() < minHeap.size()) {
                System.out.println((float)(Integer)minHeap.peek());
            } else {
                System.out.println((float)((Integer)maxHeap.peek() + (Integer)minHeap.peek())/2);
            }
        }

    }
}
