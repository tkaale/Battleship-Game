def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = []
    for element in lines:
        table.append(element.replace("\n", "").split(","))
    return table

def overwrite_table_to_file(table, file_name):
    with open(file_name, "w") as file:
        for sublist in table:
            row = ','.join(sublist)
            file.write(row + "\n")