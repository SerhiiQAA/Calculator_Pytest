from typing import Union

class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        result = x / y
        return int(result) if result.is_integer() else result
    
    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x + y
    
    def subtract(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x - y
    
    def multiply(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x * y

if __name__ == '__main__':
    calculator = Calculator()
    # Приклади використання:
    print("Add: 5 + 3 =", calculator.add(5, 3))
    print("Subtract: 5 - 3 =", calculator.subtract(5, 3))
    print("Multiply: 5 * 3 =", calculator.multiply(5, 3))
    print("Divide: 6 / 3 =", calculator.divide(6, 3))
    print("Divide: 7 / 3 =", calculator.divide(7, 3))
