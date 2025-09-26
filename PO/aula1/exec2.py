import random
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver("Rotulo qualquer", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

N = random.randint(1, 5)

Li = [random.random() for i in range(N)]
Ei = [random.random() for i in range(N)]
T = random.random()
Ti = [random.random() for i in range(N)]

lb = [0 for i in range(N)]

xi = [solver.NumVar(lb[i], Ei[i], f"x{i+1}") for i in range(N)]

ct = solver.Constraint(-solver.infinity(), T)
for i in range(N):
    ct.SetCoefficient(xi[i], Ti[i])

objective = solver.Objective()
for i in range (N):
    objective.SetCoefficient(xi[i],Li[i])
objective.SetMaximization()

result = solver.Solve()

if result != 0:
    print("infeasible")
else:
    print("Solucao encontrada:")
    print("Objetivo =", objective.Value())
    for i in range(N):
        print(f"x{i+1} = {xi[i].solution_value()}")