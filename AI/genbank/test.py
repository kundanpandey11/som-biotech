from Bio import Entrez
import os 
#Provide an email address
Entrez.email = "youremail@example.com"
#First, you may want to find out the available search fields in the 
#database you're searching (the nucleotide database contains DNA/RNA #info, so that's what we want here).
with Entrez.einfo(db="nucleotide") as handle:
    record = Entrez.read(handle)

# for field in record["DbInfo"]["FieldList"]:
#     print("%(Name)s, %(FullName)s, %(Description)s" % field)

# print(record)

###Returns a printout of search fields like this:
###ACCN, Accession, Accession number of sequence
###PACC, Primary Accession, Does not include retired secondary accessions
###GENE, Gene Name, Name of gene associated with sequence
###PROT, Protein Name, Name of protein associated with sequence
###ECNO, EC/RN Number, EC number for enzyme or CAS registry number
###PDAT, Publication Date, Date sequence added to GenBank
###
#Second, let's get all of the accession numbers for the available
#SARS-CoV-2 sequences using the ORGN field (organism) to limit the #search term
with Entrez.esearch(db="nucleotide", term="SARS-CoV-2[ORGN]", idtype="acc", retmax="10000") as handle:
    results = Entrez.read(handle)
accs = results["IdList"]#save the list of accession numbers

print(len(accs))
# print(accs[0])
print(type(results))

filename = "gene10.gbk"
if not os.path.isfile(filename):
    # create genbank file for 10 accn 
    with Entrez.efetch(db="nucleotide", id=accs[10], rettype="gb", retmode="text") as net_handle: 
            #downloading
            with open(filename, "w") as out_handle:
                out_handle.write(net_handle.read())
            print("Saved")