def draw_lake(size=4):
    print("/", end="")
    for i in range(size):
        print("----", end="")
    print("\\")
    for i in range(size):
        print("|", end="")
        for j in range(size):
            print("~ ~ ", end="")
        print("|")
    print("\\", end="")
    for i in range(size):
        print("----", end="")
    print("/")
    return
