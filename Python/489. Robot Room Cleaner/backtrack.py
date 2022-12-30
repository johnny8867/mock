# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = ((-1,0), (0,-1), (1,0), (0,1))
        visited = set()

        def backtrack(x, y, direction):
            visited.add((x,y))
            robot.clean()
            for i in range(4):
                new_dir = (direction+i) % 4
                new_x = x + directions[new_dir][0]
                new_y = y + directions[new_dir][1]
                if (new_x, new_y) not in visited and robot.move():
                    backtrack(new_x, new_y, new_dir)
                    self.go_back(robot)
                robot.turnRight()

        backtrack(0,0,0)

        #N - number of tiles in room, M - number of cell blocked
        #O(N-M), O(N-M)
        
    def go_back(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        