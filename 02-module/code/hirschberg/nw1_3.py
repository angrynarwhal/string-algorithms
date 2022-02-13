from functions1_3 import nw

# Read alphabet and scores from text file
print('Reading alphabet scores from the text files scores.txt')
f = open("scores.txt", 'r')
alphabet = f.readline()
while(alphabet[-1] in ['\n', '\r']):
    alphabet = alphabet[:-1]
f.readline()
gapPenalty = int(f.readline())
print(f'This lines gap penalty is: {gapPenalty}')
f.readline()
simMatrix = []
line = f.readline()
print('Building a matrix.')
while(line):
    row = list(int(x) for x in line.split())
    simMatrix.append(row)
    print(f'sim matrix length is now: {len(simMatrix)}')
    line = f.readline()
f.close()

# Create a 1-1 mapping from characters to integers, for simplicity in algorithm
print(f'Creating a 1-1 mapping from characters to integers, for simplicity in algorithm')
alphEnum = dict([(alphabet[i], i) for i in range(len(alphabet))])

# Load input sequences
print('Loading input sequences.')
f = open("sequences.txt", 'r')
line = f.readline()

# Open output file, in preparation for storing output alignments
print('Opening output file alignments.txt in preparation for storing output alignments.')
g = open("alignments.txt", 'w')


print('OK. This is the part in class where we are navigating two sequences at a time and matching.')
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

    # Run the NW algorithm

    print('First sequence:, {A}')
    print('Second sequence:, {B}')
    print('Calculating alignment distance by Needleman-Wunsch method...')
    
    z = nw(A, B, simMatrix, gapPenalty, alphEnum)

    print(f'Alignment of A:  {z[0]} \n')
    print(f'Alignment of B:  {z[1]} \n')
    print(f'Similarity score: {z[2]} \n')

    # Write outputs to text file
    g.write(str(z[2]) + "\n")
    g.write(z[0] + "\n")
    g.write(z[1] + "\n")
    g.write("\n")

# Close the files and finish
f.close()
g.close()
