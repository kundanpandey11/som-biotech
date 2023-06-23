# SOLUBILTY 
import deepchem as dc

# Load the built-in Delaney dataset
def create_model():
    tasks, datasets, transformers = dc.molnet.load_delaney(featurizer='GraphConv')

    # Extract the training and validation datasets
    train_dataset, valid_dataset, test_dataset = datasets

    # Define the model
    solubility_model = dc.models.GraphConvModel(n_tasks=1, mode='regression', model_dir="solubility")

    # Fit the model to the training dataset
    solubility_model.fit(train_dataset, nb_epoch=100) 
    solubility_model.save()
    return solubility_model

# Define a dummy molecule
# dummy_smiles = 'CCO'  # Replace with your own molecule SMILES

def predict_sol(smiles, model):
    featurizer = dc.feat.ConvMolFeaturizer()
    smiles_X = featurizer.featurize([smiles])
    predicted_solubility = model.predict_on_batch(smiles_X)
    print('Predicted Solubility:', predicted_solubility)
    toxicity_label = "Toxic" if predicted_solubility[0] >= 0.5 else "Non-toxic"
    print(toxicity_label)
    return predicted_solubility[0][0]

# model.restore()
# create_model()
model1 = dc.models.GraphConvModel(n_tasks=1, mode='regression', model_dir="Model_solubility")
model2= dc.models.GraphConvModel(n_tasks=12, mode='classification', model_dir="Model_toxicity")


# predict(smiles="CCOCC", model=model2)
# model.save("solubility")