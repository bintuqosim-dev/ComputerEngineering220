def read_file_sync():
    with open("file.txt", "r") as file:
        data = file.read()
    print("Fayldagi ma'lumot:", data)

read_file_sync()
