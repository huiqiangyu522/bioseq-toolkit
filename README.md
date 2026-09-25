 # BioSeq Toolkit

#### Video Demo: None

## Description

BioSeq Toolkit is a command-line program that takes DNA or RNA input and can perform functions such as calculating GC content, generating reverse complementary sequences, transcribing sequences, performing simple searches, calculating sequence length statistics, and reading FASTA files. It is used to automate the analysis of DNA sequences. It supports only FASTA-format files containing properly formatted DNA sequences, where each sequence name begins with “>”. It can be used to process any DNA sequence.


## Features


- Read DNA sequences from FASTA files
- Calculate sequence length
- Calculate GC content
- Generate reverse complement sequences
- Transcribe DNA into RNA
- Search for motifs
- Support multiple sequences in one FASTA file



## Usage


1. Prepare the FASTA file
2. Open a terminal
3. Run the program
4. Enter the motif (if your program requires it)
5. View the analysis results



## FASTA Input Format

程序接受fasta的文件内容例如：

```text
>sequence_1
ATGCGTACGTAG

>sequence_2
GGGCCCAAATTT
```

- Each sequence is identified by a header beginning with ‘>’
- Supports multiple DNA sequences
- Each DNA sequence can span multiple lines
- Allows a mix of uppercase and lowercase bases
- When an anomalous base is detected, a prompt will indicate that an anomalous base has been found and provide its location


## Output


- Sequence name
- Sequence length
- GC content
- Reverse complement
- RNA sequence
- Motif count
- Motif positions


## Project Files

###BioSeq_Toolkit.py

- Reading FASTA files
- Data processing
- Calling various analysis functions
- Outputting results

- gc_content(), accepts a sequence parameter in string format, calculates the total number of G and C bases in the sequence, determines the percentage of G and C bases in the sequence, and outputs the result as a percentage
- reverse_complement(), accepts a sequence parameter in string format, reverses the order of the sequence, and outputs a new sequence based on the rules of base complementary pairing
- transcribe(), accepts a string-formatted sequence parameter, replaces the T bases in the sequence to obtain an RNA sequence
- check_sequence(), accepts a string-formatted sequence parameter, checks for anomalous bases in the sequence, and returns the positions of the anomalous bases
- motif_search(), accepts a string-formatted sequence parameter and a motif sequence parameter, searches for the motif in the sequence, and returns the number of occurrences and their positions
- read_fasta(): Accepts a FASTA file as a parameter, reads the sequence from the file, and saves the sequence name


### test_project.py


- GC content calculation
- Reverse complement
- DNA transcription
- motif searching
- invalid input tasta file
- empty sequences


### test.fasta

This is a sample FASTA file used to test the program.



## Design Decisions

- When reading the file contents, 'read_fasta()' stores the sequence names and sequences separately in two lists. Since a FASTA file may contain multiple sequences, the sequences are stored in the lists in order as strings.
- The GC content must be calculated separately for each sequence.
- In the program, all base positions are numbered starting from 1, rather than 0, for readability.
- Each feature is implemented as a separate function to facilitate unit testing and future maintenance.
- When an invalid DNA character is encountered, the program displays a message indicating that an invalid character has been detected, along with the sequence name and position where it occurred.
- Do not use BioPython. Since the purpose of this project is to practice Python, parsing the FASTA file yourself demonstrates your ability to read files, process strings, work with dictionaries, use loops, and design functions—rather than relying on a library to handle all the core work.


## Testing

Run the Test：

python3 -m pytest test_project.py




## Author

Robert