nonlocal cycle
cycle = 0
nonlocal X
X = 1

def noop():
	cycle =+ 1

def addx(V):
	addxv = 0
	cycle =+ 2
	X =+ addxv

noop()
addx(3)
addx(-5)

print("Cycle: ", cycle)
print("Register: ", X)





