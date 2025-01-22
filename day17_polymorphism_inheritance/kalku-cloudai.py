import math
from typing import Callable, Union
from enum import Enum


class Operation(Enum):
    """Enum for basic mathematical operations"""
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'


class TrigFunction(Enum):
    """Enum for trigonometric functions"""
    SIN = 'sin'
    COS = 'cos'
    TAN = 'tan'


class Calculator:
    """Base calculator class for basic arithmetic operations"""

    @staticmethod
    def calculate(operation: Operation, x: float, y: float) -> float:
        """Performs basic arithmetic calculations"""
        operations = {
            Operation.ADD: lambda a, b: a + b,
            Operation.SUBTRACT: lambda a, b: a - b,
            Operation.MULTIPLY: lambda a, b: a * b,
            Operation.DIVIDE: lambda a, b: a / b if b != 0 else float('inf')
        }
        return operations[operation](x, y)


class ScientificCalculator(Calculator):
    """Scientific calculator with trigonometric operations"""

    def __init__(self):
        self._trig_functions = {
            TrigFunction.SIN: math.sin,
            TrigFunction.COS: math.cos,
            TrigFunction.TAN: math.tan
        }

    def trig_operation(self,
                       operation: Operation,
                       trig_func: TrigFunction,
                       angle1: float,
                       angle2: float,
                       use_degrees: bool = True) -> dict:
        """
        Performs trigonometric calculations

        Args:
            operation: Type of arithmetic operation
            trig_func: Trigonometric function to use
            angle1: First angle
            angle2: Second angle
            use_degrees: If True, converts degrees to radians

        Returns:
            Dictionary containing calculation results
        """
        try:
            # Convert degrees to radians if needed
            if use_degrees:
                angle1_rad = math.radians(angle1)
                angle2_rad = math.radians(angle2)
            else:
                angle1_rad = angle1
                angle2_rad = angle2

            # Calculate trigonometric values
            trig_func_name = trig_func.value
            trig_method = self._trig_functions[trig_func]
            value1 = trig_method(angle1_rad)
            value2 = trig_method(angle2_rad)

            # Perform the operation
            result = self.calculate(operation, value1, value2)

            return {
                'angle1': angle1,
                'angle2': angle2,
                'value1': value1,
                'value2': value2,
                'operation': operation.value,
                'trig_function': trig_func_name,
                'result': result
            }

        except ValueError as e:
            return {'error': f"Calculation error: {str(e)}"}
        except ZeroDivisionError:
            return {'error': "Division by zero error"}


def format_result(calc_result: dict) -> None:
    """Formats and prints calculation results"""
    if 'error' in calc_result:
        print(f"Error: {calc_result['error']}")
        return

    print("\n" + "=" * 40)
    trig_func = calc_result['trig_function']
    print(f"{trig_func}({calc_result['angle1']}) = {calc_result['value1']:.4f}")
    print(f"{trig_func}({calc_result['angle2']}) = {calc_result['value2']:.4f}")
    print(f"Operation: {calc_result['value1']:.4f} {calc_result['operation']} {calc_result['value2']:.4f}")
    print(f"Result: {calc_result['result']:.4f}")
    print("=" * 40 + "\n")


def main():
    calc = ScientificCalculator()

    while True:
        try:
            print("\n=== Scientific Calculator ===")
            print("1. Trigonometric Calculations")
            print("2. Exit")

            choice = input("\nSelect option (1-2): ")

            if choice == '2':
                print("Thank you for using the calculator!")
                break

            elif choice == '1':
                # Get input angles
                angle1 = float(input("Enter first angle (in degrees): "))
                angle2 = float(input("Enter second angle (in degrees): "))

                # Select trigonometric function
                print("\nSelect trigonometric function:")
                print("1. Sine (sin)")
                print("2. Cosine (cos)")
                print("3. Tangent (tan)")
                trig_choice = input("Enter choice (1-3): ")

                trig_map = {'1': TrigFunction.SIN, '2': TrigFunction.COS, '3': TrigFunction.TAN}
                selected_trig = trig_map.get(trig_choice)

                if not selected_trig:
                    print("Invalid trigonometric function selection!")
                    continue

                # Select operation
                print("\nSelect operation:")
                print("1. Addition (+)")
                print("2. Subtraction (-)")
                print("3. Multiplication (*)")
                print("4. Division (/)")
                op_choice = input("Enter choice (1-4): ")

                op_map = {
                    '1': Operation.ADD,
                    '2': Operation.SUBTRACT,
                    '3': Operation.MULTIPLY,
                    '4': Operation.DIVIDE
                }
                selected_op = op_map.get(op_choice)

                if not selected_op:
                    print("Invalid operation selection!")
                    continue

                # Perform calculation and display results
                result = calc.trig_operation(selected_op, selected_trig, angle1, angle2)
                format_result(result)

            else:
                print("Invalid option! Please try again.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()