class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = [[] for _ in range(numCourses)]

        in_degrees = [0 for _ in range(numCourses)]


        for u,v in prerequisites:
            adj_list[u].append(v)
            in_degrees[v] += 1
        
        queue = deque()

        res = []

        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                queue.append(i)
        
        while len(queue) != 0:

            curr_node = queue.popleft()

            res.append(curr_node)

            for adj_node in adj_list[curr_node]:

                in_degrees[adj_node] -= 1

                if in_degrees[adj_node] == 0:
                    queue.append(adj_node)
        

        if len(res) == numCourses:
            return True
        return False

        