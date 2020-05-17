def readIPsFromFile(fileName):
    with open(fileName) as file:
        lines = file.readlines()
    allIps = [ line.strip() for line in lines]
    return allIps
