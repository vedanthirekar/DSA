class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        def dfs(i):
            if track_course[i] == 2:
                return False
            
            if track_course[i] == 1:
                return True

            else:
                track_course[i] = 1
                for nei in graph[i]:
                    if dfs(nei):
                        return True
                track_course[i] = 2
                return False

        for a, b in prerequisites:
            graph[a].append(b)

        track_course = [0]*numCourses

        for i in range(numCourses):
            if dfs(i):
                return False
        return True

        

        