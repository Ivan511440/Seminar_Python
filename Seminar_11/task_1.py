class Arhive:
    """Архив"""
    numbers = []
    values = []
    
    def __new__(cls, number: int, value: str):
        """Расширяет метод параметрами number, value"""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        
        return instance
    
    def __init__(self, number: int, value: str):
        """Инициализирует экземпляр"""
        self.number = number
        self.value = value
    
    def __repr__(self):
        """Представление для разработчика"""
        return f'Arhive({self.number}, {self.value})'

