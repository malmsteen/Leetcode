def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    def area(x1, y1, x2, y2):
        h = y2-y1
        w = x2-x1
        return h * w

    cy1 = max(ay1, by1)
    cx1 = max(ax1, bx1)
    cy2 = min(ay2, by2)
    cx2 = min(ax2, bx2)
    s1 = area(ax1, ay1, ax2, ay2)
    s2 = area(bx1, by1, bx2, by2)
    overlap = area(cx1, cy1, cx2, cy2)
    return s1 + s2 - overlap


print(computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
