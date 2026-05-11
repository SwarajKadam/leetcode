class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    
        for i in range (0,len(gas)):
            tank = 0
            c = i    
            n = i+1  
            possible =True
            for j in range (0,len(gas)): 
                tank = tank - cost[c] + gas[c] 
                if tank<0:
                    possible = False
                    break
                c+=1
                n+=1
                if c==len(gas):
                    c=0
                if n== len(gas):
                    n=0
                

            if possible:
                return i

        return -1
                
                    
class Solution2:
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        counter =0
        current =0
        tank = 0
        c = current
    
        possible =True

        while True:
            if current == len(gas):
                break
            
            tank = tank -cost[c]+gas[c]
            if tank<0:
                    possible = False

            if not possible:
                current+=1
                counter = 0
                tank =0
                c = current
                possible =True
                continue
            c+=1
        
            if c==len(gas):
                c=0
            

            counter+=1
            if counter == len(gas):
                if possible:
                    return current
                current+=1
                counter = 0

            
            
        return -1




          
        