class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]

        def helper(candidates,target,i,curSum,temp):
            # Bounding condition
            if curSum>target:
                return  
            
            # Base case
            if curSum==target:
                self.ans.append(temp[:])
                return

            if i == len(candidates):
                return
            
            # inclusion of candidates[i]
            temp.append(candidates[i])
            helper(candidates,target,i,curSum+candidates[i],temp)
            temp.pop() # Backtrack

            # exclusion of candidates[i]
            helper(candidates,target,i+1,curSum,temp)
                    


        helper(candidates,target,0,0,[])
        return self.ans
        