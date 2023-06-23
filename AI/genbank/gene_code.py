from Bio import Entrez, SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

# Set the email address for the Entrez API
Entrez.email = "your_email@example.com"

# Search for a DNA sequence using the Entrez API
handle = Entrez.esearch(db="nucleotide", term="RB[All Fields] AND ('Homo sapiens'[Organism] OR Homo sapiens[All Fields])")
record = Entrez.read(handle)
handle.close()

# Download the DNA sequence from GenBank
handle = Entrez.efetch(db="nucleotide", id=record["IdList"][0], rettype="fasta", retmode="text")
sequence = SeqIO.read(handle, "fasta")
handle.close()

# Print the DNA sequence
print(sequence)
print(sequence.seq)


# Define the DNA sequence of the gene
# dna_sequence = "ATGAAATTTCCCGGGTTTAAAGGG"

# Create a SeqRecord object with the sequence
    # seq_record = SeqIO.SeqRecord(
    #     seq=sequence.seq,
    #     id=sequence.id,
    #     name=sequence.name,
    #     description=sequence.description,
    # )

    # # Define the start and end positions of the CDS feature
    # cds_start = 1
    # cds_end = 18

    # # Create a SeqFeature object for the CDS feature
    # cds_feature = SeqFeature(
    #     FeatureLocation(start=cds_start, end=cds_end),
    #     type="CDS",
    #     qualifiers={
    #         "gene": "gene1",
    #         "product": "Example protein",
    #     }
    # )

    # # Add the CDS feature to the SeqRecord object
    # seq_record.features.append(cds_feature)

    # # Write the SeqRecord object to a GenBank file
    # SeqIO.write(seq_record, "gene1.gbk", "genbank")