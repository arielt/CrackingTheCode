class FreqStack {
    private Map<Integer, Integer> freq;
    private Map<Integer, Stack<Integer>> group;
    int maxFreq;

    public FreqStack() {
        freq = new HashMap();
        group = new HashMap();
        maxFreq = 0;
    }
    
    public void push(int x) {
        int f = freq.getOrDefault(x, 0) + 1;
        freq.put(x, f);
        if (f > maxFreq) maxFreq = f;
        
        group.computeIfAbsent(f, z -> new Stack()).push(x);
    }
    
    public int pop() {
        int n = group.get(maxFreq).pop();
        if (group.get(maxFreq).isEmpty()) {
            // group.remove(maxFreq); // consumption of 76.29/72.73 vs 84.42/43.36
            maxFreq--;
        }
        freq.put(n, freq.get(n) - 1);
        return n;
    }
}

