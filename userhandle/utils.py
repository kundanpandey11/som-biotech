from Bio import Entrez, SeqIO
from Bio.Seq import Seq
import deepchem as dc 
from AI.deepchem.solubility import predict_sol
# from AI.deepchem.toxicity import predict_tox 





#deepchem 
#solubility 
def deepchem_predict(smiles):
    model_sol = dc.models.GraphConvModel(n_tasks=1, mode='regression', model_dir="models/Model_solubility")
    model_tox= dc.models.GraphConvModel(n_tasks=12, mode='classification', model_dir="models/Model_toxicity")

      
#genbank 
def genbank_search(query):
        Entrez.email = "admin@gmail.com"
        data = []
        handle = Entrez.esearch(db="nucleotide", term=query, retmax=20)
        search_results = Entrez.read(handle)
        handle.close()
        record_ids = search_results['IdList']
        handle = Entrez.efetch(db='nucleotide', id=record_ids, rettype='gb', retmode='text')
        records = SeqIO.parse(handle, 'gb')
        # DNA sequence
        for record in records:
            name = record.name
            description = record.description
            accession = record.annotations['accessions'][0]
            sequence = str(record.seq)
            #tropology 
            seq_object = Seq(sequence)
            # Access sequence information
            sequence_length = len(seq_object)
            sequence_topology = "linear" if sequence_length > 1 else "circular"
            # Print the sequence information
            string_sequence_trop = "{} bp {}".format(sequence_length, sequence_topology)
            # print("Length:", sequence_length, "bp")
            # print("Topology:", sequence_topology)
            data.append({
                  'name': name, 'description': description, "accession": 
                  accession, "trop": string_sequence_trop
                  })
        handle.close()
        return data
