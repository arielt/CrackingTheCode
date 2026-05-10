class Solution {
    /* recursive find: O(logN) / O(logN), 100.00% / 60.42%
    public int recFind(int[] nums, int l, int r) {
        int c = (l + r)/2;

        if (c == l || c == r) {
            return nums[l] >  nums[r] ? nums[r] : nums[l];
        }
        
        // just hack it
        if (nums[c] < nums[c-1] && nums[c] < nums[c+1] ) return nums[c];
        
        if (nums[c] > nums[l]) {
            if (nums[c] < nums[r]) {
                return nums[l]; // found
            } else {
                return recFind(nums, c+1, r); // go right
            }
        } else {
            return recFind(nums, l, c-1); // go left
        }
    }
    */
    
    public int findMin(int[] nums) {
        //return recFind(nums, 0, nums.length - 1);
        
        // O(logN) / O(1) solution
        if (nums.length == 1) return nums[0];
        
        int l = 0,
            r = nums.length - 1;
        
        if (nums[l] < nums[r]) return nums[l];
        int c = (l+r)/2;
        while (l <= r) {
            c = (l+r)/2;

            if (nums[c] > nums[c+1]) return nums[c+1];
            if (nums[c-1] > nums[c]) return nums[c];
            
            if (nums[c] > nums[0]) {
                l = c + 1;
            } else {
                r = c-1;
            }
        }
        return -1;
    }
}

