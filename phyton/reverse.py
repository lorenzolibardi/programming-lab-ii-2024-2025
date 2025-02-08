import sys

def main(fileName):
    with open(fileName, "r") as file:
        lines = [line.strip() for line in file] # rimuove l'endline
        with open(fileName + ".rev", "w") as fileW:
            for i in range (len(lines)-1, -1, -1):
                print(lines[i],file=fileW)


assert len(sys.argv)==2

main(sys.argv[1])