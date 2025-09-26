from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('modelo_generico', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

N = int(input().strip())
Ei = [float(input().strip()) for i in range(0, N)]
Li = [float(input().strip()) for i in range(0, N)]
Ti = [float(input().strip()) for i in range(0, N)]
T  = float(input().strip())

xi = [solver.NumVar(0.0, Ei[i], f"x{i+1}") for i in range(N)]

ct = solver.Constraint(-solver.infinity(), T)
for i in range(N):
    ct.SetCoefficient(xi[i], Ti[i])

objective = solver.Objective()
for i in range(N):
    objective.SetCoefficient(xi[i], Li[i])
objective.SetMaximization()

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Solucao:")
    print(f"Valor objetivo = {objective.Value():.1f}")
    for i in range(N):
        print(f"x{i+1} = {xi[i].solution_value():.1f}")
else:
    print("Sem Solucao")