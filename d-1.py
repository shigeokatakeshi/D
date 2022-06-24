# 次のコードが正しく動作するような Circle クラスを実装してください
# area は面積、 perimeter は周囲長(=円周の長さ) という意味です。
# # 半径1の円
# circle1 = Circle(radius=1)
# print(circle1.area())  # 3.14
# print(circle1.perimeter())  # 6.28

# # 半径3の円
# circle3 = Circle(radius=3)
# print(circle3.area())  # 28.27
# print(circle3.perimeter())  # 18.85

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        m_area = self.radius * self.radius * 3.14
        return m_area
    
    def perimeter(self):
        circumference = self.radius * 2 * 3.14
        return circumference


circle1 = Circle(radius=1)

print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28
