#include <vector>
#include <unordered_map>
#include <iostream>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
            unordered_map<int, int> num_to_index;  // Hash map to store number and its index
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];  // Calculate the complement of the current number
            
            // Check if the complement exists in the hash map
            if (num_to_index.find(complement) != num_to_index.end()) {
                // If found, return the indices of the two numbers
                return {num_to_index[complement], i};
            }
            
            // Otherwise, add the current number and its index to the hash map
            num_to_index[nums[i]] = i;
        }
        
        return {};  // Return an empty vector if no solution is found (should not happen as per the problem constraints)
    }
};