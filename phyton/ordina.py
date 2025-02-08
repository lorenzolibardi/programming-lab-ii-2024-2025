import sys

def main(fileName):
    with open(fileName, "r") as file:
        lines = [line.strip() for line in file] # rimuove l'endline
        lines.sort(key=len, reverse=True)
        with open(fileName + ".dec", "w") as fileW:
            for i in range (0, len(lines)):
                print(lines[i],file=fileW)


assert len(sys.argv)==2

main(sys.argv[1])