# Homework 3
# Author: Gi
# Date: September 7, 2026

highway_number = int(input("Enter a highway number: "))

if highway_number == 0 or highway_number > 999:
    print("Invalid highway number.")

elif highway_number <= 99:
    if highway_number % 2 == 0:
        print(f"Interstate {highway_number} runs east/west.")
    else:
        print(f"Interstate {highway_number} runs north/south.")

else:
    primary_highway = highway_number % 100

    if primary_highway % 2 == 0:
        direction = "east/west"
    else:
        direction = "north/south"

    print(
        f"Interstate {highway_number} is an auxiliary highway "
        f"serving I-{primary_highway}, which runs {direction}."
    )
```
