from django.shortcuts import render
from django.db.models import Sum
from userincome.models import UserIncome
from expenses.models import Expense

def balance(request):
    total_income = UserIncome.objects.filter(owner=request.user).aggregate(total_income=Sum('amount'))['total_income'] or 0
    total_expenses = Expense.objects.filter(owner=request.user).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0
    balance = total_income - total_expenses
    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance
    }
    return render(request, 'balance/index.html', context)
