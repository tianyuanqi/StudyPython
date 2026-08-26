with open("server.log", "r", encoding="utf-8") as file:
    error_count = 0
    for line in file:
        if "ERROR" in line:
            error_count += 1
            print(line.strip())

    print(f"ERROR数量:{error_count}")