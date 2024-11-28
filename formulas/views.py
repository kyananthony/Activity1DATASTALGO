from django.shortcuts import render, redirect
from .forms import FormulaForm


def input_formula(request):
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FormulaForm
        return render(request, 'formulas/input_formula.html', {'form': form})

    def success(request):
        return render(request, 'formulas/success.html')

# Create your views here.
