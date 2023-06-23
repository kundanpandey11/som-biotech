# from collections import defaultdict
import gzip

# %matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt

from Bio import SeqIO

# recs = SeqIO.parse(open('gene1.gbk'), 'genbank')
# gb_record = next(recs)
# # print(gb_record)
# # print(rec.id, rec.description, rec.seq)
# # print(rec.letter_annotations) # quality scores of our reads, per lette
# print(gb_record.features)
# # Load the GenBank record
gb_record = SeqIO.read("gene10.gbk", "genbank")

# Extract the features and their locations
features = gb_record.features
locations = [f.location for f in features]

# Create a plot of the feature locations
# fig, ax = plt.subplots()
# ax.broken_barh([(l.start, l.end - l.start) for l in locations], (0, 1), facecolors='blue')
# ax.set_xlim(0, len(gb_record))
# ax.set_xlabel("Position (bp)")
# ax.set_yticks([])
# ax.set_title("GenBank Record: {}".format(gb_record.id))
# plt.show()
