from functions1_3 import nw
from functions1_3 import forwards
from functions1_3 import backwards
from functions1_3 import hirschberg

# Read alphabet and scores from text file
with open("scores.txt", 'r') as f:
    scores_content = f.read().split('\n')
    scores_content = [line for line in scores_content if len(line) > 0]

alphabet = scores_content[0]
gapPenalty = int(scores_content[1])
simMatrix = list()

for line in scores_content[2:]:
    row = [int(x) for x in line.split()]
    simMatrix.append(row)

# Create a 1-1 mapping from characters to integers, for simplicity in algorithm
alphEnum = {alphabet[i]: i for i in range(len(alphabet))}

# Load input sequences
with open("sequences.txt", 'r') as f:
    sequences_content = f.read().split('\n')
    sequences_content = [line for line in sequences_content if len(line) > 0]

results = list()

for i in range(0, len(sequences_content), 2):
    # This loop repeats until no more input sequences are found
    # At each iteration we read the next two sequences and run the algorithm on them
    try:
        line1 = sequences_content[i]
        line2 = sequences_content[i+1]
    except IndexError:
        break

    # Run the Hirschberg algorithm
    print(f"First sequence: {line1}")
    print(f"Second sequence: {line2}")
    
    z = hirschberg(line1, line2, simMatrix, gapPenalty, alphEnum)

    print(f"Alignment of A: {z[0]}") 
    print(f"Alignment of B: {z[1]})")
    print(f"Similarity score: {z[2]}\n")

    # Store contents
    results.append(str(z[2]))
    results.append(z[0])
    results.append(z[1]) 
    results.append('')

# add newlines
results = [f"{element}\n" for element in results]

# Write to output file
with open("alignments.txt", 'w') as g:
    g.writelines(results)
