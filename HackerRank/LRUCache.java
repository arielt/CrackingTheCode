public class Node {
    public Node prev;
    public Node next;
    public int val;
    public int key;
    Node(int k, int v) {
        prev = null;
        next = null;
        key = k;
        val = v;
    }
}

class LRUCache {
    private int size;
    private int capacity;
    private HashMap<Integer, Node> map;
    Node first; //LRU
    Node last;  //one to delete

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        first = null;
        last = null;
        map = new HashMap<Integer, Node>();
    }
    
    // helpers
    private void delete(Node n) {
        // reconnect links
        if (n.prev == null) {
            first = n.next;
        } else {
            n.prev.next = n.next;            
        }
        
        if (n.next == null) {
            last = n.prev;
        } else {
            n.next.prev = n.prev;
        }      
    }
    
    private void putFirst(Node n) {
        if (first != null) {
            first.prev = n;
        }
        
        n.next = first;
        n.prev = null;
        first = n;
        
        if (last == null) {
            last = n;
        }
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            Node n = map.get(key);
            delete(n);
            putFirst(n);
            return n.val;
        } else {
            return -1;
        }
    }
    
    public void put(int key, int value) {
        Node n;
        
        if (map.containsKey(key)) {
            n = map.get(key);
            n.val = value;
            delete(n);
            putFirst(n);
        } else {
            if (map.size() >= capacity) {
              map.remove(last.key);
              delete(last);
            }

            // new element
            n = new Node(key, value);
            map.put(key, n);
            putFirst(n);
        }        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
