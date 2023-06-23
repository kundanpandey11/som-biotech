from django.shortcuts import render, redirect 
# from data.solubility import predict, create_model
from django.http import HttpResponse


def solubility_prediction(request):
    if request.method == "POST":
        smiles = request.POST['smiles']
        # if "solubility_model" not in request.session:
        #     request.session['solubility_model'] = create_model()
        # sol_model = request.session['solubility_model']
        # if request.session['solubility_model'] == None:
        #     sol_model = solubility_model

        pre_sol = "predict(smiles=smiles, model=sol_model)"
        context = {
            "solubility": pre_sol
        }
        return render(request, "dashboard.html", context)
    else: 
        return render(request, "dashboard.html")