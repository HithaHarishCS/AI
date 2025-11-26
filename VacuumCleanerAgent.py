# Dynamic Vacuum Cleaner Agent for 2x2 environment
# Rooms: A B
#        C D

# ---------------------------------------------------------
# COST RULES:
# Cleaning cost: 2 units
# Movement cost: 1 unit
# ---------------------------------------------------------

# TAKE USER INPUT FOR ROOM STATUSES
rooms = {}
for room in ["A", "B", "C", "D"]:
    status = input(f"Enter status for Room {room} (CLEAN / DIRTY): ").upper()
    if status not in ["CLEAN", "DIRTY"]:
        status = "DIRTY"
    rooms[room] = status

# TRAVEL ORDER FOR THE AGENT
order = ["A", "B", "D", "C"]
current_index = 0

# COST VARIABLES
cleaning_cost = 2
movement_cost = 1

total_cost = 0
steps = 0

print("\n=== Vacuum Cleaner Agent Started ===\n")

while True:
    room = order[current_index]
    print(f"Agent in room: {room}")
    steps += 1

    # Sense and clean
    if rooms[room] == "DIRTY":
        print("Room is DIRTY → Cleaning...")
        rooms[room] = "CLEAN"
        total_cost += cleaning_cost
    else:
        print("Room already CLEAN.")

    # Check if all clean
    if all(rooms[r] == "CLEAN" for r in rooms):
        print("\nAll rooms are CLEAN ✔")
        break

    # Move to next room
    current_index = (current_index + 1) % 4
    print(f"Moving to next room → {order[current_index]}")
    total_cost += movement_cost

    print()

print("\n=== TASK COMPLETED ===")
print(f"Total Steps Taken: {steps}")
print(f"Total Cost: {total_cost} units")
print("\nFinal Room States:", rooms)
