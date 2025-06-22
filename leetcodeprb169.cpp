//Leetcode Problem 169 Majority Element using Moore's voting algorithm
class Solution {
public:
    int majorityElement(vector<int>& nums) {

        int freq = 0, ans = 0;

        for(int i = 0; i < nums.size(); i++) {
            if(freq == 0){
                ans = nums[i];
            } if(ans == nums[i]){
                freq++;
            } else {
                freq--;
            }
        }

        return ans;
        
    }
};

//Leetcode Problem 169 Majority Element using Brute force method
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();

        for(int val : nums){
            int freq = 0;

            for(int el : nums) {
                if(el == val) {
                    freq++;
                }
            }
            if(freq > n/2){
                return val;
            }
        }

        return -1; 
    }   
};
