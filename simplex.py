from scipy.optimize import linprog

# Coefficients of the objective function (negated for maximization)
c = [-2, -3]

# Coefficients of the inequality constraints (left-hand side)
A = [
    [1, 1],
    [2, 1]
]

# Right-hand side of the inequality constraints
b = [4, 5]

# Bounds for the variables (x >= 0, y >= 0)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

# Print the results
print('Optimal value:', -result.fun)
print('x:', result.x[0])
print('y:', result.x[1])