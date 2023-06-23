"""
Script that trains graph-conv models on Tox21 dataset.
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

np.random.seed(123)
import tensorflow as tf

tf.random.set_seed(123)
import deepchem as dc
from deepchem.molnet import load_tox21
from deepchem.models.graph_models import GraphConvModel

model_dir = "Model_toxicity"

# Load Tox21 dataset
tox21_tasks, tox21_datasets, transformers = load_tox21(featurizer='GraphConv')
train_dataset, valid_dataset, test_dataset = tox21_datasets
print(train_dataset.data_dir)
print(valid_dataset.data_dir)

# Fit models
metric = dc.metrics.Metric(
    dc.metrics.roc_auc_score, np.mean, mode="classification")

# Batch size of models
batch_size = 50

model = GraphConvModel(
    len(tox21_tasks), batch_size=batch_size, mode='classification', model_dir=model_dir )

model.fit(train_dataset, nb_epoch=10)

print("Evaluating model")
train_scores = model.evaluate(train_dataset, [metric], transformers)
valid_scores = model.evaluate(valid_dataset, [metric], transformers)

print("Train scores")
print(train_scores)

print("Validation scores")
print(valid_scores)