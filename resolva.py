def remove_git_conflicts(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if ">>>>>>> origin/main" in line:
                continue
            elif "<<<<<<< HEAD" in line:
                continue
            elif "=======" in line:
                continue
            else:
                file.write(line)

if __name__ == "__main__":
    filename = input("Digite o nome do arquivo: ")
    remove_git_conflicts(filename)
    print("Conflitos do Git removidos com sucesso!")
