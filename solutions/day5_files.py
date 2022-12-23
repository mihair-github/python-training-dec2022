# 1. Write a Python program that reads file content and displays the number of
# lines that were read.

filename = 'README.md'
lines_count = 0
with open(filename) as f:
    for line in f:
        lines_count += 1
print(f'Number of lines in {filename}: {lines_count}')


# 2. Write a Python program to append text into a file and display the new
# content.

with open(filename, 'a+') as f:
    f.write('New text')
    f.seek(0)
    for line in f:
        print(line, end='')


# 3. Write a function grep that receives text and file as parameters and returns
# a list with all the lines in the file containing text.

def grep(text, file):
    lines_matching = []
    with open(filename) as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


# 4. Write another function grepinto that receives text, infile and outfile as
# parameters and writes to outfile the lines in infile that contain text. Open
# both files within one with statement.

def grep_into(text, infile, outfile):
    with open(infile) as fin, open(outfile, 'w') as fout:
        for line in f:
            if text in line:
                fout.write(line)
