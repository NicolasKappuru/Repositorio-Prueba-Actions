class Division:
    def __init__(self):
        pass

    def dividir(self, a: int, b: int) -> float:
        """
        Divide dos numeros

        Args:
            a (int): dividendo
            b (int): divisor

        Return:
            Retorna la division entre a y b
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        else:
            return a / b
