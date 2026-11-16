# PROGRAM: PHYSICS CALCULATOR USING PYTHON

# Function to calculate speed
def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    if time != 0:
        result = distance / time
        print("Speed =", result, "m/s")
    else:
        print("Time cannot be zero")


# Function to calculate velocity
def velocity():
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s²): "))
    t = float(input("Enter time (s): "))
    result = u + (a * t)
    print("Final velocity =", result, "m/s")


# Function to calculate acceleration
def acceleration():
    v = float(input("Enter final velocity (m/s): "))
    u = float(input("Enter initial velocity (m/s): "))
    t = float(input("Enter time (s): "))
    if t != 0:
        result = (v - u) / t
        print("Acceleration =", result, "m/s²")
    else:
        print("Time cannot be zero")


# Function to calculate force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration_value = float(input("Enter acceleration (m/s²): "))
    result = mass * acceleration_value
    print("Force =", result, "N")


# Function to calculate work done
def work():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    result = force_value * distance
    print("Work done =", result, "J")


# Function to calculate power
def power():
    work_done = float(input("Enter work done (J): "))
    time = float(input("Enter time (s): "))
    if time != 0:
        result = work_done / time
        print("Power =", result, "W")
    else:
        print("Time cannot be zero")


# Main program
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Velocity")
    print("3. Acceleration")
    print("4. Force")
    print("5. Work Done")
    print("6. Power")

    choice = input("\nSelect an operation (1-6): ")

    if choice == "1":
        speed()
    elif choice == "2":
        velocity()
    elif choice == "3":
        acceleration()
    elif choice == "4":
        force()
    elif choice == "5":
        work()
    elif choice == "6":
        power()
    else:
        print("Invalid choice!")

    again = input("\nDo you want to perform another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
