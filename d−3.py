# 次のコードが正しく動作するような Square クラスを実装してください
# diagonal は 対角線(の長さ) という意味です。
# square1 = Square(side=1.5)
# print(square1.area())  # 2.25
# print(square1.diagonal())  # 2.12

# square2 = Square(side=15)
# print(square2.area())  # 225
# print(square2.diagonal())  # 21.21
import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        s_area = self.side**2
        return s_area

    def diagonal(self):
        s_line = self.side**2 + self.side**2
        ss_line = math.sqrt(s_line)
        ss_line = round((ss_line), 2)
        return ss_line


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
