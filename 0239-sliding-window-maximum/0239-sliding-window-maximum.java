class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        int n = nums.length;
        int[] res = new int[n - k + 1];
        int idx = 0;
        for(int i = 0; i < n; i++) {
            while(!deque.isEmpty() && deque.peek() < i - k + 1){
                deque.poll();
            }
            while(!deque.isEmpty()&& nums[deque.peekLast()]<nums[i]){
                deque.pollLast();
            }
            deque.offer(i);
            //因为单点 当i增长到符合第一个k范围时候，每滑动异步都将队列头节点放入结果
            if(i>=k-1){
                res[idx++]=nums[deque.peek()];
            }
        }
        return res;
    }
}