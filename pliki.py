# 'r'
# open
# for reading(default)
# 'w'
#     open
#     for writing, truncating the file first
# 'x'
# create
# a
# new
# file and open
# it
# for writing
# 'a'
#     open
#     for writing, appending to the end of the file if it exists
# 'b'
# binary
# mode
# 't'
# text
# mode(default)
# '+'
# open
# a
# disk
# file
# for updating(reading and writing)

# domyslnie po zakonczeniu operacji plik zostaje zamkniety
with open('test.log', "w", encoding='utf-8') as f:
    f.write("Radek\n")
    f.write("Zenek\n")
    f.write("Tomek\n")
    f.write("Michał\n")

with open('test.log', 'a', encoding='utf-8') as file:
    file.write("DOśdane\n")


with open('test.log', 'r', encoding='utf-8') as fh:
    lines = fh.read()
    print(lines)

for i, l in enumerate(lines):
    print(i, l)