import fileinput

fileToSearch = "../reversestockdictionary.js"
textToSearch = "&#39;"
textToReplace = "\\'"

with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(textToSearch, textToReplace), end = '')
