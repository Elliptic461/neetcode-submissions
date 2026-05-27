class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list of prereqs
        prereq = {c:[] for c in range(numCourses)}
        # This is same as for i in range(numCourses):
        # prereq[i] = []

        for crs, pre in prerequisites:
            prereq[crs].append(pre) 
        
        # course has 3 possible states:
        # Visited -> crs has been added to output
        # Visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        result = []
        # Visiting set
        cycle = set()
        # A node you have process
        seen = set()

        def dfs(cur):
            if cur in cycle:
                return False
            if cur in seen:
                return True
            
            cycle.add(cur)

            for child in prereq[cur]:
                if not dfs(child):
                    return False
            
            cycle.remove(cur)
            seen.add(cur)
            result.append(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result

