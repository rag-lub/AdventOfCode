def ReadInput(filename):
    inp1 = {}
    with open(filename,"r") as f:
        for line in f:
            values = line.strip().split(")")
            inp1[values[1]]=values[0]
    return inp1

def main():
    orbits = ReadInput("input.txt")
    counter = 0
    for object in orbits.keys():
        cur_orbiter = orbits[object]
        counter+=1
        while cur_orbiter != "COM":
            cur_orbiter = orbits[cur_orbiter]
            counter+=1
    return counter

print(main())