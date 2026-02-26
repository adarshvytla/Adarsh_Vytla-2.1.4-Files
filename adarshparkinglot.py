parkingLot = [[0,0,0,0,0], [0,2,1,1,2], [0,1,1,2,1], [0,0,0,0,0], [0,1,2,2,1]]
freeSpaces = 0
for row in parkingLot:
    freeSpaces += row.count(2)
    for col in row:
        print(col, end = " ")
    print()
print("Available Spaces (marked as 2): " + str(freeSpaces))


