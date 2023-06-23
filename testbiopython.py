from Bio import Entrez, SeqIO

# Set the email address for the Entrez API
Entrez.email = "your_email@example.com"

# Search for a DNA sequence using the Entrez API
handle = Entrez.esearch(db="nucleotide", term="RB Homo sapiens")
record = Entrez.read(handle)
handle.close()

# Download the DNA sequence from GenBank
handle = Entrez.efetch(db="nucleotide", id=record["IdList"][19], rettype="fasta", retmode="text")
sequence = SeqIO.read(handle, "fasta")
handle.close()

# Print the DNA sequence
print(sequence.seq)
# print(len(record['IdList']))
# print(record)
