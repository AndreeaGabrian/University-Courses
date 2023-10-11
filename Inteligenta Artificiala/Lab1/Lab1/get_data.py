
def read_data_from_file(filename):
    objects = []
    with open(filename) as file:
        count = 0
        for line in file:
            count += 1
            line = line.strip()
            line = line.split(" ")
            line = [elem for elem in line if elem != ""]
            if count == 1:
                objects_number = int(line[0])
            elif count != 1 and len(line) == 1:
                bag_max_weight = int(line[0])
            else:
                objects.append((int(line[1]), int(line[2])))

    return objects_number, bag_max_weight, objects




