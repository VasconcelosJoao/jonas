#1 Passo - Importação da biblioteca e instanciação do solver
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('rotulo', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#2 Passo - Parametrização do problema

#f - 3x1 + x2
#   f1x1 + f2x2
f = [3, 1]

# 0 <= x1 <= 1
# lb1 <= x1 <= ub1
# 0 <= x2 <= 2
# lb2 <= x2 <= ub2
lb = [0, 0]
ub = [1, 2]

# x1+x2 <= 2
a = [1, 1]
b = 2

#3 Passo - Definição das variáveis de decisão

# x1 e x2
# xi = []
# for i in range(len(f)):
#    xi.append(solver.NumVar(lb[i], ub[i], f"x{i+1}"))

xi= [solver.NumVar(lb[i], ub[i], f"x{i+1}") for i in range(len(f))]

#4 Passo - Definição das restrições

# x1 + x2 <= 2

ct=solver.Constraint(-solver.infinity(), b)

for i in range(len(a)):
    ct.SetCoefficient(xi[i], a[i])

#5 Passo - Definição da função objetivo

# max 3x1 + x2

objective = solver.Objective()
for i in range(len(f)):
    objective.SetCoefficient(xi[i], f[i])
objective.SetMaximization()


#6 Passo - Chamada do solver
resultado = solver.Solve()

if resultado != 0:
    print("Sem Solução - Infeasible")
else:
    print("Solução Encontrada")
    print(f"Valor da Função Objetivo: {objective.Value()}")
    for i in range(len(f)):
        print(f"x{i+1} = {xi[i].solution_value()}")

