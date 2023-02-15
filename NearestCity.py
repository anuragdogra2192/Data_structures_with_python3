'''
Given a list of points, find the nearest points that shares either an x or a y coordinate with the queried point.

The distance is denoted on a Euclidean plane: the difference in x plus the difference in y.

Input

numOfPoints, an integer representing the number of points;

points, a list of strings representing the names of each point [i];

xCoordinates, a list of integers representing the X coordinates of each point[i];

yCoordinates, a list of integers representing the Y coordinates of each point[i];

numOfQueriedPoints, an integer representing the number of points queried;

queriedPoints, a list of strings representing the names of the queried points.

Output

Return a list of strings representing the name of the nearest points that shares either an x or a y coordinate with the queried point.

Example 1:

Input:

numOfPoints = 3

points = ["p1","p2","p3"]

xCoordinates = [30, 20, 10]

yCoordinates = [30, 20, 30]

numOfQueriedPoints = 3

queriedPoints = ["p3", "p2", "p1"]

Output:

["p1", NONE, "p3"]

Example 2:

Input:

numOfPoints = 5

points = ["p1", "p2","p3", "p4", "p5"]

xCoordinates = [10, 20, 30, 40, 50]

yCoordinates = [10, 20, 30, 40, 50]

numOfQueriedPoints = 5

queriedPoints = ["p1", "p2", "p3", "p4", "p5"]

Output

[NONE, NONE, NONE, NONE, NONE]

'''
# Time Complexity O(numOfQueriedPoints*numOfPoints)
# Space Complexity O(numOfQueriedPoints)
numOfPoints = 3
points = ["p1","p2","p3"]
xCoordinates = [30, 20, 10]
yCoordinates = [30, 20, 30]
numOfQueriedPoints = 3
queriedPoints = ["p3", "p2", "p1"]

def nearestCity(points, xCoordinates, yCoordinates, numOfPoints, numofQueriedPoints, queriedPoints):
    Output = []
    for i in range(0, numOfQueriedPoints):
        nearest = 0
        temp = 0
        n_point = None
        for j in range(0, numOfPoints):
            if queriedPoints[i] != points[j]:
                dx = xCoordinates[i] - xCoordinates[j]
                dy = yCoordinates[i] - yCoordinates[j]
                if (dx == 0 or dy == 0):
                    temp = dx*dx + dy*dy
                    if (nearest == 0 or nearest>temp):
                        nearest = temp
                        n_point = points[j]
        Output.append(n_point)

    return Output

print(nearestCity(points, xCoordinates, yCoordinates, numOfPoints, numOfQueriedPoints, queriedPoints))

numOfPoints = 5
points = ["p1", "p2","p3", "p4", "p5"]
xCoordinates = [10, 20, 30, 40, 50]
yCoordinates = [10, 20, 30, 40, 50]
numOfQueriedPoints = 5
queriedPoints = ["p1", "p2", "p3", "p4", "p5"]
print(nearestCity(points, xCoordinates, yCoordinates, numOfPoints, numOfQueriedPoints, queriedPoints))

numOfPoints = 6
points = ["p1", "p2","p3", "p4", "p5", "p6"]
xCoordinates = [30, 20, 10, 20, 20, 10]
yCoordinates = [30, 20, 30, 10, 30, 20]
numOfQueriedPoints = 5
queriedPoints = ["p1", "p2", "p3", "p4", "p5"]
print(nearestCity(points, xCoordinates, yCoordinates, numOfPoints, numOfQueriedPoints, queriedPoints))
