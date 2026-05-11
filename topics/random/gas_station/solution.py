class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        tank = 0
        current_tank =0
        start =0 
        for i in range (0,len(gas)):
            gain = gas[i] -cost[i]
            tank += gain
            current_tank +=gain
            
            if current_tank<0:
                start = i+1
                current_tank =0

        if tank <0:
            return -1
                


        return start