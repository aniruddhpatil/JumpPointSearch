import math

def heuristic(a, b, hchoice):
    if hchoice == 1:
        xdist = math.fabs(b[0] - a[0])
        ydist = math.fabs(b[1] - a[1])
        if xdist > ydist:
            return 14 * ydist + 10 * (xdist - ydist)
        else:
            return 14 * xdist + 10 * (ydist - xdist)
    if hchoice == 2:
        return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def blocked(cX, cY, dX, dY, matrix):
    if cX + dX < 0 or cX + dX >= matrix.shape[0]:
        return True
    if cY + dY < 0 or cY + dY >= matrix.shape[1]:
        return True
    if dX != 0 and dY != 0:
        if matrix[cX + dX][cY] == 1 and matrix[cX][cY + dY] == 1:
            return True
        if matrix[cX + dX][cY + dY] == 1:
            return True
    else:
        if dX != 0:
            if matrix[cX + dX][cY] == 1:
                return True
        else:
            if matrix[cX][cY + dY] == 1:
                return True
    return False


def dblock(cX, cY, dX, dY, matrix):
    if matrix[cX - dX][cY] == 1 and matrix[cX][cY - dY] == 1:
        return True
    else:
        return False