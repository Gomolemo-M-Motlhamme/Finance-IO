from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Income, Expense
from .forms import  Update_E,Update_I

def Index(request):
    income = Income.objects.all()
    expense = Expense.objects.all()
    return render(request, "index.html", {'income': income, 'expense': expense})

# add view
def add_E(request):
    if request.method == 'POST':
        expense = request.POST.get('expense')
        amount = request.POST.get('amount')
        date = request.POST.get('date')

        new_expense = Expense(expense=expense, amount=amount, date=date)
        new_expense.save()

        return redirect('/Index')
    return redirect('error_page')

# add view
def add_I(request):
    if request.method == 'POST':
        income = request.POST.get('income')
        amount = request.POST.get('amount')

        new_income = Income(income=income, amount=amount)
        new_income.save()

        return redirect('/Index')
    return redirect('error_page')

# update view
def update_I(request, pk):
    current = Income.objects.get(id=pk)
    form = Update_I(request.POST or None, instance=current)
    if form.is_valid():
        form.save()
        return redirect('/Index')
    return render(request, 'Pages/update_I.html', {'form': form})

# update view
def update_E(request, pk):
    current = Expense.objects.get(id=pk)
    form = Update_E(request.POST or None, instance=current)
    if form.is_valid():
        form.save()
        return redirect('/Index')
    return render(request, 'Pages/update_E.html', {'form': form})


# delete view
def delete_E(request, pk):
    delete = Expense.objects.get(id=pk)
    delete.delete()
    return redirect('/Index')

# delete view
def delete_I(request, pk):
    delete = Income.objects.get(id=pk)
    delete.delete()
    return redirect('/Index')