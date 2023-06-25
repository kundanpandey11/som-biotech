from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.http import HttpResponse
from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen
from rdkit.Chem import AllChem
import deepchem as dc 
from AI.deepchem.toxicity import predict_tox
from AI.deepchem.solubility import predict_sol


def deepchem_qsar(request):
    if request.method == "POST":
        smiles_ = request.POST['smiles']
        smiles = smiles_.upper()
        # print("smiles :::::",smiles)
        # context = {"smiles":smiles}
        request.session['smiles'] = smiles
        context = {"smiles": smiles}
        try: 
            tox = predict_tox(smiles=smiles)
            sol = predict_sol(smiles=smiles)
            toxicity_label = "Toxic" if tox[0] >= 0.5 else "Non-toxic"
            

            context.update({"tox": tox[0], "sol":sol, "toxicity_label": toxicity_label})
        except Exception :
            messages.error(request, "Something went wrong! Please try again in some time.")
        return render(request, "bargraph/deepchem_qsar.html", context)
    else:
        smiles = request.session['smiles']
        return render(request, "bargraph/deepchem_qsar.html", {"smiles": smiles })


        # if "solubility_model" not in request.session:
        #     request.session['solubility_model'] = create_model()
        # sol_model = request.session['solubility_model']
        # if request.session['solubility_model'] == None:
        #     sol_model = solubility_model

    #     pre_sol = "predict(smiles=smiles, model=sol_model)"
    #     context = {
    #         "solubility": pre_sol
    #     }
    #     return render(request, "dashboard.html", context)
    # else: 
    #     return render(request, "dashboard.html")
    

# predict mol weight, LogP (partition coefficient), Topological polar surface area
def rdkit_predict_mw(request):

    if request.method == "POST":
        smiles_ = request.POST['smiles']
        smiles = smiles_.upper()
        print("smiles :::::",smiles)
        context = {"smiles":smiles}
        request.session['smiles'] = smiles

        try:
            
            molecule = Chem.MolFromSmiles(smiles)
            # Perform any necessary preparations
            molecule = Chem.AddHs(molecule)  # Add hydrogens to the molecule
            AllChem.EmbedMolecule(molecule)  # Generate 3D coordinates for the molecule
            AllChem.UFFOptimizeMolecule(molecule)  # Optimize the 3D structure

            # Calculate descriptors
            mw = Descriptors.MolWt(molecule)  # Molecular weight
            logp = Descriptors.MolLogP(molecule)  # LogP (partition coefficient)
            tpsa = Descriptors.TPSA(molecule)  # Topological polar surface area
            context.update(
                {"mw":mw,"logp":logp, "tpsa":tpsa,
                "smiles":smiles}
                )
            # context = 
            request.session['rdkit_context_mw'] = context
            # print(f"Molecular Weight: {mw:.2f} g/mol")
            # print(f"LogP: {logp}")
            # print(f"TPSA: {tpsa:.2f} Å²")
            # print(mw, logp, tpsa)
        except Exception:
            messages.error(request, "Invalid Smiles!")
            # return render(request, "bargraph/rdkit_mol_wgt.html", context)
        return render(request, "bargraph/rdkit_mol_wgt.html", context)

    else: 
        context = request.session['rdkit_context_mw']
        smiles = request.session['smiles']
        context.update({"smiles": smiles})
        return render(request, "bargraph/rdkit_mol_wgt.html", context)
    

# predict if the molecule is hydrogen acceptor and donor 
def rdkit_predict_hydrogen(request):
    if request.method == "POST":
        smiles_ = request.POST['smiles']
        smiles = smiles_.upper()
        print("smiles :::::",smiles)

        context = {"smiles":smiles}
        request.session['smiles'] = smiles
        
        try:

            molecule = Chem.MolFromSmiles(smiles)

            # Calculate additional descriptors
            hba = Descriptors.NumHAcceptors(molecule)  # Number of hydrogen bond acceptors
            hbd = Descriptors.NumHDonors(molecule)  # Number of hydrogen bond donors
            rotb = Descriptors.NumRotatableBonds(molecule)  # Number of rotatable bonds
 
            context.update({
                "HBD": hbd, "HBA": hba, 
                "RB" : rotb
            })
            request.session['rdkit_context_hydrogen'] = context
        except Exception as e: 
            messages.error(request, "Invalid Smiles!")
        return render(request, "bargraph/rdkit_hydrogen.html", context)
    else: 
        context = request.session['rdkit_context_hydrogen']
        smiles = request.session['smiles']
        context.update({"smiles": smiles})
        return render(request, "bargraph/rdkit_hydrogen.html", {"smiles":smiles})


def splicing(request):
    return render(request, "bargraph/piechart.html")