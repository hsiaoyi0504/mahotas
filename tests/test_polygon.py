import numpy as np
import mahotas.polygon
from mahotas.polygon import fill_polygon, fill_convexhull

def test_polygon():
    polygon = [(10,10), (10,20), (20,20)]
    canvas = np.zeros((40,40), np.bool)
    fill_polygon(polygon, canvas)
    assert canvas.sum() == (10*10-10)/2


def test_convex():
    polygon = [(100,232), (233,222), (234,23), (555,355), (343,345), (1000,800)]
    canvas = np.zeros((1024, 1024), np.bool)
    mahotas.polygon.fill_polygon(polygon, canvas)
    canvas2 = mahotas.polygon.fill_convexhull(canvas)
    # The overlap isn't perfect. There is a slight sliver. Fixing it is not
    # worth the trouble for me (LPC), but I'd take a patch
    assert (canvas & ~canvas2).sum() < 1024

def test_convex3():
    f = np.array([
        [False, False, False, False],
        [False,  True,  True, False],
        [False,  True, False, False],
        [False, False, False, False]], dtype=bool)
    assert np.all(fill_convexhull(f) == f)

def test_fill3():
    canvas = np.zeros((4,4), bool)
    # This polygon also has a horizontal and a vertical edge
    polygon = [(1, 1), (1, 2), (2, 1)]
    assert mahotas.polygon.fill_polygon(polygon, canvas).sum()