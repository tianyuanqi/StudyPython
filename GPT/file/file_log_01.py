with open("server.log", "r", encoding="utf-8") as file:
    lines = file.readlines()

    error_count = 0
    for line in lines:
        if "ERROR" in line:
            error_count += 1
            print(line.strip())

    print(f"ERROR数量:{error_count}")