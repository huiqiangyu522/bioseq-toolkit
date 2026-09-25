import pytest
from BioSeq_Toolkit import gc_content, read_fasta, reverse_complement, transcribe, motif_search, check_sequence

def test_gc_content():
    assert gc_content("GGCCAATT") ==  "50.0%"

def test_gc_content_invalid():
    assert gc_content("") == 0

def test_read_fasta():
    sequences, names = read_fasta("test.fasta")
    assert isinstance(sequences, list)
    assert isinstance(names, list)
    assert len(sequences) == len(names)
    assert names[0].startswith("SEQ")
    assert "ATGC" in sequences[0]

def test_invalid_fasta():
    with pytest.raises(SystemExit):
        read_fasta("invalid")

def test_reverse_complement():
    assert reverse_complement("GGCCAATT") == "AATTGGCC"

def test_transcribe():
    assert transcribe("GGCCAATT") == "GGCCAAUU"

def test_motif_search():
    assert motif_search("GGCCAATT", "GC") == [2]
    assert motif_search("GGCCAATT", "GA") == []

def test_check_sequence():
    assert check_sequence("GGCCAATT") == []
    assert check_sequence("DOG") == [1, 2]