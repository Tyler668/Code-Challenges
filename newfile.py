# will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) ➞ True

# will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70, 80, 90, 200]) ➞ False

# will_fit(["L", "L", "M"], [56, 62, 84, 90]) ➞ True

holdCapacities = {
    'S': 50,
    'M': 100,
    'L': 200
}


def will_fit(holds, cargo):
    holdWeights = [holdCapacities[x] for x in holds]
    totalCap = 0

    for i in holdWeights:
        totalCap += i

    totalCargo = 0

    for j in cargo:
        totalCargo += j

    print(totalCap, totalCargo)

    if totalCap >= totalCargo:
        return True
    else:
        return False
        
    # print(holdWeights)
    # holdWeights = holdWeights.sort()

    # cargo = cargo.sort()


will_fit(["L", "L", "M"], [56, 62, 84, 90])
