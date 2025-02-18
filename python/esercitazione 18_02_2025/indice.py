# istruzioni a https://elearning.di.unipi.it/mod/page/view.php?id=22210

import os
import sys


def main(src, dest):
    dest_dir = os.getcwd() + "/" + dest
    
    if(os.path.exists(dest_dir)):
        print(f"ERRORE: La directory di destinazione {dest} esiste già")
        exit(1)

    os.mkdir(dest_dir)
    src_dir = os.getcwd() + "/" + src
    files = explore(src_dir)
    occurrencies = {}

    for file in files:
        file_name = os.path.basename(file)
        occ = occurrencies.get(file_name, 0)
        occurrencies[file_name] = occ + 1
    
    for file in files:
        file_name = os.path.basename(file)
        first_char = (file_name)[0].lower()
        
        dest_subpath = os.path.join(dest_dir, first_char)
        if(os.path.exists(dest_subpath) == False):
            os.mkdir(dest_subpath)

        final_path = os.path.join(dest_subpath, file_name)

        if occurrencies[file_name] == 1:
            if not os.path.exists(final_path):
                os.link(file, final_path)
                print(f"{file} {final_path}")
        else:
            for i in range (1, occurrencies[file_name] + 1):
                final_path = os.path.join(dest_subpath, file_name+f".{i}")
                if not os.path.exists(final_path):
                    os.link(file, final_path)
                    print(f"{file} {final_path}")


def explore(elem): # albero di files -> array
    if os.path.isfile(elem): return [elem]
    files = []
    for x in os.listdir(elem):
        if x.startswith("."): continue

        filepath = os.path.join(elem, x) # calcolo dir corrente + nuovo file/dir
        if os.path.islink(filepath): continue # salto i link simbolici
        
        if os.path.isdir(filepath):
            files.extend(explore(filepath))  
        else:
            files.append(filepath)
    return files


assert len(sys.argv) == 3
main(sys.argv[1], sys.argv[2])