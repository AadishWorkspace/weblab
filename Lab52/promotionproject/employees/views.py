from django.shortcuts import render
from .forms import PromotionForm
import datetime

def check_promotion(request):
    result = ""
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            doj = form.cleaned_data['date_of_joining']
            today = datetime.date.today()
            experience = (today - doj).days / 365.25
            result = "YES" if experience >= 5 else "NO"
    else:
        form = PromotionForm()

    return render(request, 'promotion.html', {'form': form, 'result': result})
