

class Calculator:
    ans = 0

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @classmethod
    def set_ans(cls, ans):
        cls.ans = ans

    @staticmethod
    def largest(a,b,c,d):
        return max(a,b,c,d)

    @staticmethod
    def smallest(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def calculate_factorial(number):
        if number < 0:
            raise ValueError("Faktoriál záporného čísla neexistuje.")

        if number == 0:
            return 1

        product = 1
        for i in range(1, number + 1):
            product *= i

        return product




print(Calculator.add(3, 5))
print(Calculator.ans)

c = Calculator()
print(c.ans)
c.ans = 100
Calculator.ans = 110
print(Calculator.ans)
print(c.ans)

c.set_ans(500)
print(Calculator.ans)