
import deepchem as dc



def predict_tox(smiles):
    model = dc.models.GraphConvModel(n_tasks=12, mode='regression', model_dir="Model_toxicity")
    featurizer = dc.feat.ConvMolFeaturizer()
    smiles_X = featurizer.featurize([smiles])
    predicted_toxicity = model.predict_on_batch(smiles_X)
    print('Predicted Solubility:', predicted_toxicity)
    toxicity_label = "Toxic" if predicted_toxicity[0] >= 0.5 else "Non-toxic"
    print(toxicity_label)
    return predicted_toxicity[0][0]


def predict_tox(smiles):
    model = dc.models.GraphConvModel(n_tasks=12, mode='classification', model_dir="Troxicity_model")
    featurizer = dc.feat.ConvMolFeaturizer()
    smiles_X = featurizer.featurize([smiles])
    predicted_toxicity = model.predict_on_batch(smiles_X)
    print('Predicted toxicity:', predicted_toxicity[0][0][0])
    return predicted_toxicity[0][0]

# model.restore()
# create_model()

