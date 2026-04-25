class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> curr=new ArrayList<>();
        List<List<Integer>> ans =new ArrayList<>();
        rec(nums,0,curr,ans);
        return ans;
        
        
    }
    public static void rec(int[] num,int idx,List<Integer> curr,List<List<Integer>> ans){
        if(idx==num.length){
            ans.add(new ArrayList<Integer>(curr));
            return;
        }
        curr.add(num[idx]);
        rec(num,idx+1,curr,ans);
        curr.remove(curr.size()-1);
        rec(num,idx+1,curr,ans);
    }
}