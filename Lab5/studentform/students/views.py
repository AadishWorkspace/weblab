# students/views.py
from django.shortcuts import render
from .forms import StudentForm

def student_entry(request):
    result = ""
    percentage = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            total = data['english'] + data['physics'] + data['chemistry']
            percentage = round(total / 3, 2)
            result = (
                f"Name: {data['name']}\n"
                f"DOB: {data['dob']}\n"
                f"Address: {data['address']}\n"
                f"Contact: {data['contact']}\n"
                f"Email: {data['email']}\n"
                f"Marks - English: {data['english']}, "
                f"Physics: {data['physics']}, Chemistry: {data['chemistry']}\n"
            )
    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form, 'result': result, 'percentage': percentage})
