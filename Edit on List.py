
result_list = []

data_list = [["Jack", "223", "LA"], ["Albert", "224", "Ny"], ["George", "225", "London"], ["Jack", "226", "Chicago"],
["George", "227", "NY"], ["Jack", "228", "Paris"]]
name = input("enter a name you want to edit or remove :")
for item in data_list:
    if name in item:
        result_list.append(item)
    else:
        pass

print(result_list)

if len(result_list) == 1:
    change = input("choose what you want to do ( edit / remove ): ")
    if change == "edit":
        new_address = input("enter a new address:")
        for item in result_list:
            item[2] = new_address
    elif change == "remove":
        for item in result_list:
            data_list.remove(item)
    else:
        pass
elif len(result_list) == 0:
    print("This name does not exist!")
else:
    ID = input("enter the id:")
    change = input("choose what you want to do ( edit / remove ):")
    for item in result_list:
        if ID in item:
            if change == "edit":
                new_address = input("enter a new address:")
                item[2] = new_address
            elif change == "remove":
                data_list.remove(item)
            else:
                break
        else:
            pass

print(data_list)
