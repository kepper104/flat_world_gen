from os import SEEK_END
ended = False
created = False

print("To create/open file, type 'create file_name'")
print("To add layer, type 'add'")
print("To end file creation, type 'end'")
def trim_last_symbol():
    with open(file_name, 'rb+') as filehandle:
        filehandle.seek(-1, SEEK_END)
        filehandle.truncate()
def open_file():
    global file
    file = open(file_name,'a')
    print("Created file " + file_name)

def add_line():
    block, height = map(str,input("Block, Lay height: ").split())
    print(f"Added {height} layers of {block}")
    file.write(f"{height}*minecraft:{block},")

def end_creation():
    global file
    biome = input("Enter biome:  ")
    structures = input("Enter needed structures (example: mineshaft village): ").split()
    file.close()
    trim_last_symbol()
    with open(file_name, 'a') as file:
        file.write(";" + "minecraft:" + biome + ";")
        for item in structures:
            file.write(item + ",")
    trim_last_symbol()
    print("File created!")
    

while not ended:
    action = input()
    if action == "add":
        if created == False:
            print("You first need to create or open file!")
        else:
            add_line()
    elif action[:6] == "create":
        global file_name
        file_name = action[7:] + ".txt"
        created = True
        open_file()
    elif action == "end":
        if created == False:
            print("You first need to create or open file!")
        else:
            end_creation()
            ended = True
        
        
    else:
        print("Unknown command, try again")

    
# minecraft:bedrock,2*minecraft:dirt,minecraft:grass_block;minecraft:plains;village