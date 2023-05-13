import numpy as np
from fractions import Fraction

"""
example input
ax by cz n (dont expect me expecting anything other than this specific input, im dumdum)
sistem inkonsisten hasil inf
salah input hasil nan
"""

class Eq:
    def __init__(self, z, arr):
        self._z = z
        self._arr = arr

    def countY(self):
        # ganti sisi
        # jika negatif
        if self._arr[1][2] < 0:
            # jadi posisif
            self._arr[1][2] = abs(self._arr[1][2])
            self._y = (self._arr[1][3] + self._z * self._arr[1][2]) / self._arr[1][1]
        # jika positif
        else:
            # jadi negatif
            self._arr[1][2] = -abs(self._arr[1][2])
            # ax by cz = n
            # y = (cz + n) / b
            self._y = (self._arr[1][3] + self._z * self._arr[1][2]) / self._arr[1][1]
        self.countX()

    def countX(self):
        # (left) ax + by + cz = (right) n
        left = self._y * self._arr[0][1] + self._z * self._arr[0][2]
        if left < 0:
            left = abs(left)
        else:
            left = -abs(left)
        self._x = (self._arr[0][3] + left) / self._arr[0][0]
        self.terminal()

    def toFraction(self, data):
        return str(Fraction(data.item()).limit_denominator(5))

    def terminal(self):
        print(f'Nilai x: {self.toFraction(self._x)}, Nilai y: {self.toFraction(self._y)}, Nilai z: {self.toFraction(self._z)}')
        # hasil semua
        print(f'Nilai x: {self._x}, Nilai y: {self._y}, Nilai z: {self._z}')

def eqSeperate(eq):
    arr = eq.split(" ")
    # valueless dict (like my life)
    result = {'x': None, 'y': None, 'z': None, 'n': None}
    for item in arr:
        if 'x' in item:
            # jika huruf di depan x angka
            if item[0].isdigit():
                result['x'] = intp(item)
            # jika negatif
            elif '-' in item[0]:
                # abs() = nilai absolut
                result['x'] = -abs(intp(item, True))
            # jika tidak ada
            else:
                result['x'] = 1
        elif 'y' in item:
            if item[0].isdigit():
                result['y'] = intp(item)
            elif '-' in item[0]:
                result['y'] = -abs(intp(item, True))
            else:
                result['y'] = 1
        elif 'z' in item:
            if item[0].isdigit():
                result['z'] = int(intp(item))
            elif '-' in item[0]:
                result['z'] = -abs(intp(item, True))
            else:
                result['z'] = 1
        else:
            result['n'] = int(item)
    return result


def toMatrix(a, b, c):
    # 2d array
    arr = np.array([[a['x'], a['y'], a['z'], a['n']], [b['x'], b['y'], b['z'], b['n']],
                    [c['x'], c['y'], c['z'], c['n']]], dtype='float32')
    return calculate(arr)


def calculate(arr):
    print(arr)
    # first step (column pertama)
    # baris 2 = baris 2 - x.baris 1 = n2 - x.n1
    # dengan x = arr[1][0] / arr[0][0]
    x = arr[1][0] / arr[0][0]
    # validation function (later)
    print(x)
    arr[1] = [(arr[1][0] - x * arr[0][0]), (arr[1][1] - x * arr[0][1]), (arr[1][2] - x * arr[0][2]),
              (arr[1][3] - x * arr[0][3])]
    print(arr)
    # second step
    # baris 3 = baris 3 - x.baris 1 = n3 - x.n1
    x = arr[2][0] / arr[0][0]
    print(x)
    arr[2] = [(arr[2][0] - x * arr[0][0]), (arr[2][1] - x * arr[0][1]), (arr[2][2] - x * arr[0][2]),
              (arr[2][3] - x * arr[0][3])]
    print(arr)

    # third step
    # baris 3 = baris 3 - x.baris 2 = n3 - x.n2
    x = arr[2][1] / arr[1][1]
    print(x)
    print(arr[2][3], arr[1][3])
    arr[2] = [0, (arr[2][1] - x * arr[1][1]), (arr[2][2] - x * arr[1][2]), (arr[2][3] - (x * arr[1][3]))]
    print(arr)
    # (method to change entire array) arr[0] = [1,2,3,4]
    # last step
    z = arr[2][3] / arr[2][2]
    eq = Eq(z, arr)
    eq.countY()

def intp(item, abs=False):
    if abs == False:
        return int(item[0: len(item) - 1])
    return int(item[1: len(item) - 1])


def main():
    print(
        'Info: \npattern: ax by cz n, expected error: inkonsisten = hasil inf/divide zero error'
        ', salah input = hasil nan atau valueError\n')
    eq1 = input('persamaan 1: ')
    eq2 = input('persamaan 2: ')
    eq3 = input('persamaan 3: ')
    a, b, c = eqSeperate(eq1), eqSeperate(eq2), eqSeperate(eq3)
    return toMatrix(a, b, c)


if __name__ == "__main__":
    main()