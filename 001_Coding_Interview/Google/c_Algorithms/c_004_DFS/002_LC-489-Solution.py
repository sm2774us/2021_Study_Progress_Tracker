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

    # Solution: DFS + Backtracking
    #
    # Different from regular dfs to visit all, the robot move() function needs to be called,
    # backtrack needs to move() manually and backtracking path should not be blocked by visited positions.
    #
    # - IMPORTANT: Mark on the way by using set, but `backtrack directly without re-check against set`
    # - Backtrack: turn 2 times to revert, move 1 step, and turn 2 times to revert back.
    #
    # TC: O(4^(N-M))    - because for each cell the algorithm checks 4 directions
    # SC: O(N-M)        - to track visited cells
    #
    # Video Explanation: https://www.youtube.com/watch?v=-1P3VP7LH0I (python)
    #                    https://www.youtube.com/watch?v=VQp7pfij7_Q (java)
    #                    https://github.com/shehabic/java-algorithms/blob/master/src/solutions/RobotRoomCleaner.java (java)
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # Left, Up, Right, Down
        self.dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
        self.visited = set()
        self.backtrack(0, 0, 0, robot)

    def goBack(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(self, r, c, d, robot):
        self.visited.add((r, c))
        robot.clean()

        # move in all directions
        for dd in range(4):
            new_d = (d + dd) % 4
            new_r, new_c = r + self.dirs[new_d][0], c + self.dirs[new_d][1]

            if (new_r, new_c) not in self.visited and robot.move():
                # visit next branch
                self.backtrack(new_r, new_c, new_d, robot)
                self.goBack(robot)

            # rotate 90 degrees to visit that branch
            robot.turnRight()
