from functions1_3 import nw
from functions1_3 import forwards
from functions1_3 import backwards
from functions1_3 import hirschberg

# Read alphabet and scores from text file
print('Hirschberg: Reading alphabet scores from the text files scores.txt')
f = open("scores.txt", 'r')
alphabet = f.readline()
while(alphabet[-1] in ['\n', '\r']):
    alphabet = alphabet[:-1]
f.readline()
gapPenalty = int(f.readline())
print(f'Hirschberg: This lines gap penalty is: {gapPenalty}')
f.readline()
simMatrix = []
line = f.readline()
print('Hirschberg: Building a matrix.')
while(line):
    row = list(int(x) for x in line.split())
    simMatrix.append(row)
    line = f.readline()
f.close()

# Create a 1-1 mapping from characters to integers, for simplicity in algorithm
print(f'Hirschberg: Creating a 1-1 mapping from characters to integers, for simplicity in algorithm')
alphEnum = dict([(alphabet[i], i) for i in range(len(alphabet))])

# Load input sequences
print('Hirschberg: Loading input sequences.')
f = open("sequences.txt", 'r')
line = f.readline()

# Open output file, in preparation for storing output alignments
print('Opening output file alignments.txt in preparation for storing output alignments.')
g = open("alignments.txt", 'w')


print('OK. Hirschberg: This loop repeats until no more input sequences are found At each iteration we read the next two sequences and run the algorithm on them')
while(line):
    # This loop repeats until no more input sequences are found
    # At each iteration we read the next two sequences and run the algorithm on them
    A = line
    while(A[-1] in ['\n', '\r']):
        A = A[:-1]
    B = f.readline()
    while(B[-1] in ['\n', '\r']):
        B = B[:-1]
    f.readline()
    line = f.readline()

    # Run the Hirschberg algorithm

    print(f'First sequence: {A}')
    print(f'Second sequence: {B}')
    print('Calculating alignment distance by Hirschberg method...')
    
    z = hirschberg(A, B, simMatrix, gapPenalty, alphEnum)

    print(f"Alignment of A: {z[0]} \n ")  
    print(f"Alignment of B: {z[1]} \n ")
    print(f"Similarity score: {z[2]} \n ")

    # Write outputs to text file
    g.write(str(z[2]) + "\n")
    g.write(z[0] + "\n")
    g.write(z[1] + "\n")
    g.write("\n")

# Close the files and finish
f.close()
g.close()
