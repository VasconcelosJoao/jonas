from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('modelo_pl', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

f  = [3, 5]

lb = [0, 0]
ub = [solver.infinity(), solver.infinity()]

A = [
    [1, 0],
    [0, 2],
    [3, 2],
]
b = [4, 12, 18]

xi = [solver.NumVar(lb[i], ub[i], f"x{i+1}") for i in range(len(f))]

for j in range(len(A)):
    ct = solver.Constraint(-solver.infinity(), b[j])
    for i in range(len(f)):
        ct.SetCoefficient(xi[i], A[j][i])

objective = solver.Objective()
for i in range(len(f)):
    objective.SetCoefficient(xi[i], f[i])
objective.SetMaximization()

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Solucao:")
    print(f"Valor objetivo = {objective.Value():.1f}")
    for i in range(len(f)):
        print(f"x{i+1} = {xi[i].solution_value():.1f}")
else:
    print("Sem Solucao")