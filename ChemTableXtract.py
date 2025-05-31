from chempy.util import periodic

# Get user input
n = int(input("Enter number to see the table: "))

# Print header
print("Atomic No.\tName\t\tSymbol\t\tMass")

# Loop through elements
for i in range(1, n + 1):
    print(i, end="\t\t")

    # Adjust spacing based on name length
    if len(periodic.names[i]) > 7:
        print(periodic.names[i], end="\t")
    else:
        print(periodic.names[i], end="\t\t")

    # Print symbol and atomic mass
    print(periodic.symbols[i], end="\t\t")
    print(periodic.relative_atomic_masses[i])
