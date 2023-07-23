##TO DO
epsilon = 1.0
while 1.0 + epsilon != 1.0:
    machine_epsilon= epsilon
    epsilon /= 2.0

print("マシンイプシロン:", machine_epsilon)
