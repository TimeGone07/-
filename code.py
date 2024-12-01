import gurobipy as grb
from gurobipy import *

# 创建模型
m = grb.Model("mip1")

# 设置变量
x = m.addVar(vtype=GRB.BINARY, name="x")
y = m.addVar(vtype=GRB.BINARY, name="y")
z = m.addVar(vtype=GRB.BINARY, name="z")

# 设置目标函数
m.setObjective(x + y + 2 * z, GRB.MAXIMIZE)

# 加约束
m.addConstr(x + 2 * y + 3 * z <= 4, "c0")
m.addConstr(x + y >= 1, "c1")

#设置不输出日志
m.setParam('outPutFlag', 0)
m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print('Obj:', m.objVal)
