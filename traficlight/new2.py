# Read data from data.txt
with open("data.txt", "r") as file:
    data = file.readlines()

print(data)

# Define expected sequences for each color
expected_data = {
    "red": "1, 0, 0, 0",
    "yellow": "0, 1, 0, 0",
    "green": "0, 0, 1, 0",
    "green_left": "0, 0, 0, 1",
    "none": "0, 0, 0, 0",
}

# Verify if recorded data matches the expected sequence
for line in data:
    color, sequence = line.split("\n")
    if sequence != expected_data[color]:
        print(f"Error: Traffic light is not working correctly for {color} signal.")
