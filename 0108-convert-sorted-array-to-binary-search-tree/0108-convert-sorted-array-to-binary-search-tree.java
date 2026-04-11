/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        TreeNode root = traversal(nums,0,nums.length-1);
        return root;

        
    }
    public TreeNode traversal(int[] nums,int left,int right){
        //终止条件
        if(left>right) return null;
        int mid = left + ((right-left)>>1);
        //根节点 取中间数 然后返回
        TreeNode  root = new TreeNode(nums[mid]);
        //递归左边的 用左子树来接收
        root.left = traversal(nums,left,mid-1);
        root.right = traversal(nums,mid+1,right);
        return root;

    }
}