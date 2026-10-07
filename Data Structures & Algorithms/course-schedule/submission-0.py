class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # First declaring the dequeue 
        from collections import deque

        queue = deque()
        # then we need to declare a count and graph variable # populate with the counts and graphs using pre-requisities
        count = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            count[course] += 1
            graph[pre].append(course)
        
        # then we need to create a final variable to equate with the numCourses
        finalvar = 0
        

        # Now we need to append the queue with no pre-requisite course 
        for course in range(numCourses):
            if count[course] == 0:
                queue.append(course)
        
        # after that create a while loop of dequeue

        while queue:

            # now we need to popleft the queue
            course = queue.popleft()

            # increment the final variable with one 
            finalvar += 1
            
            # now we need to reduce the count by seeing the dependents in the graph list 
            for dependent in graph[course]:
                count[dependent] -=1

                # then we need to check if that dependents is zero then we need to append them into the queue
                if count[dependent] == 0:
                    queue.append(dependent)
            
        # after end of the queue check the final with numCourses 

        return finalvar == numCourses
        