# Cost of one tile
cost_of_one_tile = None

while cost_of_one_tile is None or not cost_of_one_tile.isdigit() or cost_of_one_tile == "0":
    cost_of_one_tile = input("Cost of one(1) tile: ")

    if not cost_of_one_tile.isdigit():
        print("Cost must be a digit!")
    elif cost_of_one_tile == "0":
        print("Cost must be greater than 0")
    else:
        pass

cost_of_one_tile = int(cost_of_one_tile)


# Area of one tile
area_one_one_tile = None

while area_one_one_tile is None or not area_one_one_tile.isdigit() or area_one_one_tile == "0":
    area_one_one_tile = input("Area of one(1) tile: ")

    if not area_one_one_tile.isdigit():
        print("Area must be a digit!")
    elif area_one_one_tile == "0":
        print("Area must be greater than 0")
    else:
        pass

area_one_one_tile = int(area_one_one_tile)

# Width of room
width_of_floor = None

while width_of_floor is None or not width_of_floor.isdigit() or width_of_floor == "0":
    width_of_floor = input("Width of floor to calculate: ")

    if not width_of_floor.isdigit():
        print("Width of floor must be a digit!")
    elif width_of_floor == "0":
        print("Width of floor must be greater than 0")
    else:
        pass

width_of_floor = int(width_of_floor)

height_of_floor = None

while height_of_floor is None or not height_of_floor.isdigit() or height_of_floor == "0":
    height_of_floor = input("Height of floor to calculate: ")

    if not height_of_floor.isdigit():
        print("Height of floor must be a digit!")
    elif height_of_floor == "0":
        print("Height of floor must be greater than 0")
    else:
        pass

height_of_floor = int(height_of_floor)

area_of_floor_plan = width_of_floor * height_of_floor

no_of_tiles_needed = area_of_floor_plan / area_one_one_tile

total_cost_of_tiles_for_floor = cost_of_one_tile * no_of_tiles_needed


def main():
    r = f"""
    FROM THE DATA PROVIDED:\n 
    Area of floor: {f"{area_of_floor_plan}m3"}
    Total cost of tiles: {f"NGN{total_cost_of_tiles_for_floor}"}
    Number of Tiles needed: {f"{round(no_of_tiles_needed)} pieces of tiles needed"}
    """

    return r


if __name__ == "__main__":
    print(main())






