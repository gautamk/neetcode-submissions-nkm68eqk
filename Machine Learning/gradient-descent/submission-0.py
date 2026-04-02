class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        minimizer = init
        derivative = lambda x: 2 * x
        for _ in range(iterations):
            minimizer = minimizer - learning_rate * derivative(minimizer)
        return round(minimizer, 5)

