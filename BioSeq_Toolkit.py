import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 dna_tools.py <fasta_file>")
        sys.exit(1)

    filename = sys.argv[1]
    sequences, names = read_fasta(filename)
    ext = Path(filename).suffix.lower()

    if ext != ".fasta":
        print("Error: The input file must be in FASTA format.")
        sys.exit(1)

    for seq, name in zip(sequences, names):
        positions = check_sequence(seq)
        print(f"Sequence name: {name}")
        if positions:
            print(f"Found abnormal base at position: {', '.join(map(str, positions))}")
        print(f"length: {len(seq)}")
        print(f"GC Content: {gc_content(seq)}")
        print(f"Reverse Complement: {reverse_complement(seq)}")
        print(f"Transcribed: {transcribe(seq)}")
        print()

    motif = input("Enter a motif to search for: ").upper()
    for seq, name in zip(sequences, names):
        positions = motif_search(seq, motif)
        print(f"Sequence name: {name}")
        if positions:
            print(f"Motif: {motif}")
            print("Count:", len(positions))
            print(f"Motif found at positions: {', '.join(map(str, positions))}")
            print()
        else:
            print("Motif not found.")
            print()

def gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return f"{(gc_count / len(sequence)) * 100:.1f}%" if len(sequence) > 0 else 0

def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in reversed(sequence))

def transcribe(sequence):
    return sequence.replace('T', 'U')

def read_fasta(filename):
    sequences = []
    name = []
    current_seq = ""
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip().upper()
                if line.startswith(">"):
                    if current_seq:
                        sequences.append(current_seq)
                    name.append(line[1:])  # Store the sequence name (without the '>')
                    current_seq = ""
                else:
                    current_seq += line
            if current_seq:
                sequences.append(current_seq)
        return sequences, name
    except FileNotFoundError:
        sys.exit("File Not Found")

def check_sequence(sequence):
    positions = [i + 1 for i,c in enumerate(sequence) if c not in "ATGC"]
    return positions

def motif_search(sequence, motif):
    positions = []
    motif_length = len(motif)
    for i in range(len(sequence) - motif_length + 1):
        if sequence[i:i + motif_length] == motif:
            positions.append(i + 1)  # 1-based indexing
    return positions

if __name__ == "__main__":
    main()