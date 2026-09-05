from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from checkins.models import MoodEntry
from checkins.forms import MoodEntryForm

def home(requests):
    # return HttpResponse("Welcome to my website")
    return render(requests, "checkins/home.html")


def get_form(requests):
    if requests.method == 'POST':
        my_form = MoodEntryForm(requests.POST)
        print(my_form)
        if my_form.is_valid():
            mood = my_form.save(commit=False)
            mood.user = requests.user  
            mood.save()
        
            return redirect('report')
    else:
        my_form = MoodEntryForm()

    return render(
        requests,
        "checkins/entry_form.html",
        {"django_form": my_form}
    )


@login_required
def report(requests):
    # entry = MoodEntry.objects.all()
    print(requests.user, requests.user.is_staff)
    entry = MoodEntry.objects.filter(user=requests.user)

    return render(
        requests,
        "checkins/report.html",
        # selected_date, low_only, avg_score
        {"entries": entry, "count": entry.count()}
    )
def aboutus(requests):
    return render(
        requests,"checkins/about.html",

    )
@login_required
def logout_confirm(request):
    if request.method == 'POST':
        # خروج کاربر
        logout(request)
        return redirect('login')  # بعد از خروج به صفحه ورود برود
    
    # نمایش صفحه تأیید خروج (GET)
    return render(request, 'checkins/logout_confirm.html')