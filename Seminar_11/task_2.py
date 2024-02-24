class Rectangle:
    """Прямоугольник"""
    def __init__(self, a: int, b: int = None): # type: ignore
        """Инициализирует объект прямоугольника"""
        self.a = a
        self.b = a if b is None else b
        
    def perimeter(self):
        """Расчитывает периметр"""
        return 2 * (self.a + self.b)
    
    def area(self):
        """Расчитывает площадь"""
        return self.a * self.b
    
    def __add__(self, other):
        """Сложение периметров"""
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)
    
    def __sub__(self, other):
        """Вычитание периметров"""
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min((self.a, self.b, other.puple, other.b)) 
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)
        