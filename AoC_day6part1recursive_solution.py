import time
def ReadInput(filename):
    inp1 = {}
    with open(filename,"r") as f:
        for line in f:
            values = line.strip().split(")")
            inp1[values[1]]=values[0]
    return inp1

def recur(dc,orbiter):
    if orbiter == "COM":
        return 0
    else:
        return 1+recur(dc,dc[orbiter])

def main_rec():
    orbits = ReadInput("input.txt")
    counter = 0
    for object in orbits.keys():
        counter +=recur(orbits,object)
    return counter

def main_wh():
    orbits = ReadInput("input.txt")
    counter = 0
    for object in orbits.keys():
        cur_orbiter = orbits[object]
        counter+=1
        while cur_orbiter != "COM":
            cur_orbiter = orbits[cur_orbiter]
            counter+=1
    return counter
t0=time.time()
a = main_rec()
t1=time.time()
t3=time.time()
b = main_wh()
t4=time.time()

print(f"Answer for recursive soution:{a}, total run time ={t1-t0}")
print(f"Answer for iterative soution:{b}, total run time ={t3-t4}")
