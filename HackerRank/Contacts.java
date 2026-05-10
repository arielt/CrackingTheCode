import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * https://www.hackerrank.com/challenges/contacts
 */
public class Solution {

    public static class TrieNode {
        private TrieNode parent;
        private TrieNode[] children;
        private boolean isLeaf; //Quick way to check if any children exist
        private boolean isWord; //Does this node represent the last character of a word
        private char character; //The character this node represents
        private int count;

        /**
         * Constructor for top level root node.
         */
        public TrieNode() {
           children = new TrieNode[26];
           isLeaf = true;
           isWord = false;
           count = 0;
        }

        /**
         * Constructor for child node.
         */
        public TrieNode(char character) {
            this();
            this.character = character;
            this.count = 1;
        }

        /**
         * Adds a word to this node. This method is called recursively and
         * adds child nodes for each successive letter in the word, therefore
         * recursive calls will be made with partial words.
         * @param word the word to add
         */
        protected void addWord(String word) {
            isLeaf = false;
            int charPos = word.charAt(0) - 'a';

            if (children[charPos] == null) {
                children[charPos] = new TrieNode(word.charAt(0));
                children[charPos].parent = this;
            } else {
                children[charPos].count++;
            }

            if (word.length() > 1) {
                children[charPos].addWord(word.substring(1));
            } else {
                children[charPos].isWord = true;
            }
        }

        protected int queryCount(String word) {
            int charPos = word.charAt(0) - 'a';

            if ((word.length() == 1) && (children[charPos] != null)) {
                return children[charPos].count;
            } else if (children[charPos] == null)
                return 0;
            else
                return children[charPos].queryCount(word.substring(1));
        }

        /**
         * Returns the child TrieNode representing the given char,
         * or null if no node exists.
         * @param c
         * @return
         */
        protected TrieNode getNode(char c) {
           return children[c - 'a'];
       }
   }

    public static class Trie {
        private TrieNode root;

        /**
         * Constructor
         */
        public Trie() {
            root = new TrieNode();
        }

        /**
         * Adds a word to the Trie
         * @param word
         */
        public void addWord(String word) {
            root.addWord(word.toLowerCase());
        }

        public int queryCount(String word) {
          if (word.length() == 0)
            return 0;
        else
            return root.queryCount(word.toLowerCase());
       }
   }

    public static void main(String[] args) {
        Trie trie = new Trie();

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String op = sc.next();
            String word = sc.next();
            if (op.equals("add")) {
                trie.addWord(word);
            } else {
                System.out.println(trie.queryCount(word));
            }
        }
    }
}
