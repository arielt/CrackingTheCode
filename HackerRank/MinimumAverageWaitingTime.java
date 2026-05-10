import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/minimum-average-waiting-time
 */
public class Solution {

    public static class XTask {
        public final long start;
        public final long length;

        XTask(long start, long length) {
            this.start = start;
            this.length = length;
        }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();

        // all customers
        PriorityQueue<XTask> customers = new PriorityQueue<XTask>(n, new Comparator<XTask>() {
            public int compare(XTask task1, XTask task2) {
                return (int)(task1.start - task2.start);
            }
        });

        // read all customers
        for (int i=0; i<n; i++) {
            customers.add(new XTask(sc.nextLong(), sc.nextLong()));
        }

        long currentTime = 0;
        long delay = 0;
        int index = 0;
        XTask candidate = null;

        // customers already waiting
        PriorityQueue<XTask> waiting = new PriorityQueue<XTask>(n, new Comparator<XTask>() {
            public int compare(XTask task1, XTask task2) {
                return (int)(task1.length - task2.length);
            }
        });

        while(true) {

            // enter customers to wait
            while (index < n) {
                candidate = customers.peek();
                if (candidate.start <= currentTime) {
                    waiting.add(customers.remove());
                    index++;
                } else {
                    break;
                }
            }

            if (!waiting.isEmpty()) {
                candidate = waiting.remove();
                delay += currentTime + candidate.length - candidate.start;
                currentTime += candidate.length;
            } else {
                if (index != n) {
                    currentTime = customers.peek().start;
                }
            }

            if (index == n && waiting.isEmpty()) {
                break;
            }
        }

        System.out.println(delay/n);
    }
}
