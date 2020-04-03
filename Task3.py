import numpy as np


class NVector:
    def __init__(self, components):
        self._components = np.array(components)

    def __iter__(self):
        return iter(self._components)

    def __str__(self):
        return str(tuple(self))

    def __len__(self):
        return len(self._components)

    def __eq__(self, other):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))

    def __abs__(self):
        return np.math.sqrt(sum(x * x for x in self))

    def __sub__(self, other):
        new_vector = []
        for first_components, second_components in zip(self._components, other._components):
            new_vector.append(first_components - second_components)
        return NVector(new_vector)

    def __sum__(self, other):
        new_vector = []
        for first_vector, second_vector in zip(self._components, other._components):
            new_vector.append(first_vector + second_vector)
        return NVector(new_vector)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_coordinates = []
            for coordinate in self._components:
                new_coordinates.append(coordinate * other)
            return NVector(*new_coordinates)
        elif isinstance(other, NVector):
            return sum(first * second for first, second in zip(self._components, other._components))


if __name__ == "__main__":
    n1 = NVector([1, 2, 3])
    n2 = NVector([1, 1, 1])
    print(NVector.__sub__(n1, n2))
