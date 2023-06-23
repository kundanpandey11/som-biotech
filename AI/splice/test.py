from keras.models import load_model
from pkg_resources import resource_filename
from spliceai.utils import one_hot_encode
import numpy as np

input_sequence = 'CGATCTGACGTGGGTGTCATCGCATTATCGATATTGCAT'
# Replace this with your custom sequence

def splice(dna):
    context = 10000
    paths = 'models/spliceai{}.h5'.format(5) 
    models = load_model(resource_filename('spliceai', paths)) 
    x = one_hot_encode('N'*(context//2) + input_sequence + 'N'*(context//2))[None, :]
    y = models.predict(x)

    acceptor_prob = y[0, :, 1]
    donor_prob = y[0, :, 2]
    acceptor = round(max(acceptor_prob), 3)
    donor = round(max(donor_prob), 3)
    neutral = 100.0 - (acceptor - donor)
    return (acceptor, donor, neutral)