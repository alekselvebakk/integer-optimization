from pyomo.environ import *

bokstav = ['A', 'E', 'I', 'L', 'M', 'N', 'O', 'P', 'T', 'V']
print(bokstav)
print("--------------------------------------------")

N=10

xindx = range(N+1)

model = ConcreteModel(name="VismaProblem")

model.x = Var(xindx, within=NonNegativeIntegers, bounds=(0,9))

model.Obj = Objective(expr= 
1000*(model.x[7]-model.x[4])
+100*(model.x[8]-model.x[7])
+10*(model.x[9]+model.x[5]+model.x[1]+model.x[6]-model.x[10])
+(model.x[4]+model.x[8]+2*model.x[3]- model.x[2]))

# Constraints



model.constraint01 = Constraint(expr=
model.x[0]+model.x[1]+model.x[2]+model.x[3]+model.x[4]+model.x[5]+model.x[6]+model.x[7]+model.x[8]+model.x[9]==45)
model.constraint=Constraint(expr=model.x[0]!=model.x[1])



opt = SolverFactory("glpk")
opt.solve(model)
for i in range(1,N+1):
    print("***")
    print("x[",i,"]",value(model.x[i]))