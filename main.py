fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

total = 0.0
count = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(":")
        num = float(line[pos+1:])
        total = total + num
        count = count + 1

if count > 0:
    avg = total / count
    print("Average spam confidence:", avg)
else:
    print("No spam confidence lines found")