def add(x, y):
            return x + y

    def subtract(x, y):
                return x - y

        def multiply(x, y):
                    return x * y

            def divide(x, y):
                        if y != 0:
                                        return x / y
                        else:
                                        return "Erreur : division par zéro impossible"

                                def power(x, y):
                                            return x ** y

                                    def calculate(operator, x, y):
                                                if operator == '+':
                                                                return add(x, y)
                                                elif operator == '-':
                                                                return subtract(x, y)
                                                elif operator == '*':
                                                                return multiply(x, y)
                                                elif operator == '/':
                                                                return divide(x, y)
                                                elif operator == '^':
                                                                return power(x, y)
                                                else:
                                                                return "Opération invalide"

                                                        print("Sélectionnez l'opération:")
                                                        print("+ : Addition")
                                                        print("- : Soustraction")
                                                        print("* : Multiplication")
                                                        print("/ : Division")
                                                        print("^ : Puissance")

                                                        operator = input("Entrez l'opérateur: ")
                                                        num1 = float(input("Entrez le premier nombre: "))
                                                        num2 = float(input("Entrez le deuxième nombre: "))

                                                        result = calculate(operator, num1, num2)
                                                        print(f"{num1} {operator} {num2} = {result}")

                                    
