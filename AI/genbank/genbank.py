# get data from genbank 
# display names of the gene structure 
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

# Define the DNA sequence of the gene
dna_sequence = "ATGAAATTTCCCGGGTTTAAAGGG"

# Create a SeqRecord object with the sequence
seq_record = SeqIO.SeqRecord(
    seq=dna_sequence,
    id="gene1",
    name="gene1",
    description="Example gene",
)

# Define the start and end positions of the CDS feature
cds_start = 1
cds_end = 18

# Create a SeqFeature object for the CDS feature
cds_feature = SeqFeature(
    FeatureLocation(start=cds_start, end=cds_end),
    type="CDS",
    qualifiers={
        "gene": "gene1",
        "product": "Example protein",
    }
)

# Add the CDS feature to the SeqRecord object
seq_record.features.append(cds_feature)

# Write the SeqRecord object to a GenBank file
SeqIO.write(seq_record, "gene1.gbk", "genbank")
