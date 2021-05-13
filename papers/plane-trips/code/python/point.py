import numpy as np


class Point(np.ndarray):
    """
    n-dimensional point used for locations.
    inherits +, -, * (as dot-product)
    > p1 = Point([1, 2])
    > p2 = Point([4, 5])
    > p1 + p2
    Point([5, 7])
    See ``test()`` for more usage.
    """
    def __new__(cls, input_array=(0, 0)):
        """
        :param cls:
        :param input_array: Defaults to 2d origin
        """
        obj = np.asarray(input_array).view(cls)
        return obj

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def z(self):
        """
        :return: 3rd dimension element. 0 if not defined
        """
        try:
            return self[2]
        except IndexError:
            return 0

    def __eq__(self, other):
        return np.array_equal(self, other)

    def __ne__(self, other):
        return not np.array_equal(self, other)

    def __iter__(self):
        for x in np.nditer(self):
            yield x.item()


    def dist(self, other):
        """
        Both points must have the same dimensions
        :return: Euclidean distance
        """
        return np.linalg.norm(self - other)


def test():
    v1 = Point([1, 2, 3])
    v2 = Point([4, 5, 7])
    v3 = Point([4, ])
    sum12 = Point([5, 7, 10])
    dot12 = Point([4, 10, 21])

    # Access
    assert v2.x == 4
    assert v2.y == 5
    assert v2.z == 7
    assert v3.z == 0
    assert Point().x == 0
    assert v2[0] == 4
    assert v1[-1] == 3  # Not needed but inherited
    assert [x for x in v2] == [4, 5, 7], "Iteration should return all elements"

    # Operations
    assert v1 + v2 == sum12
    assert v1 * v2 == dot12
    assert v1.dist(v2) ** 2 == 34
    assert v1 != v2
    assert v2.size == 3, "v2 should be a 3d point"

    print ("pass")


if __name__ == "__main__":
    test()
