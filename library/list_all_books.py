import os
import sys
rootdir = "./"

readme_str = '# IT e-books collection \r\n ---------- \r\n'
file_tree_str = ""

all_book = []

for dir in os.listdir(rootdir):
    if os.path.isdir(dir) and dir != r".git":
        readme_str += "## " + dir +"\r\n"
        file_tree_str += dir + "\r\n"
        for file in os.listdir(dir):
            if file in all_book:
                print("Duplicate book. Book Name: " + dir + "/" + file)
                sys.exit(1)

            if os.path.isfile(os.path.join(rootdir, dir, file)):
                readme_str += file + "\r\n"
                file_tree_str += "    " + file + "\r\n"
                all_book.append(file)

print(file_tree_str)
print("Total books: " + str(len(all_book)))


readme_file = open(r"readme.md", "w")
readme_file.write(readme_str)
readme_file.close()