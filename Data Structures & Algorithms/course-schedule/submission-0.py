class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course,prereq in prerequisites:
            graph[prereq].append(course)

        UNVISITED,VISITING,DONE = 0,1,2
        state = [UNVISITED]*numCourses

        def dfs(node):
            if state[node] == VISITING:
                return True
            if state[node] == DONE:
                return False
            
            state[node] = VISITING

            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True
            
            state[node] = DONE
            return False

        for course in range(numCourses):
            if state[course] == UNVISITED:
                if dfs(course):
                    return False
        
        return True






