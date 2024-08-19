def solve(wire):
    if wire.isdigit():
        return int(wire)

    if isinstance(wires[wire], int):
        return wires[wire]

    instruction = wires[wire]

    if isinstance(instruction, str):
        wires[wire] = solve(instruction)

    elif len(instruction) == 1:
        wires[wire] = solve(instruction[0])

    elif len(instruction) == 2:
        operation, operand = instruction
        if operation == "NOT":
            wires[wire] = ~solve(operand) & 0xFFFF

    elif len(instruction) == 3:
        left, operation, right = instruction
        if operation == "AND":
            wires[wire] = solve(left) & solve(right)
        elif operation == "OR":
            wires[wire] = solve(left) | solve(right)
        elif operation == "LSHIFT":
            wires[wire] = solve(left) << solve(right)
        elif operation == "RSHIFT":
            wires[wire] = solve(left) >> solve(right)

    return wires[wire]


wires = {}

with open("2015/day7/input") as file:
    for line in file:
        parts = line.replace("->", "").strip().split()
        if len(parts) == 2:
            wires[parts[1]] = parts[0]
        else:
            wires[parts[-1]] = parts[:-1]

print(solve("a"))
