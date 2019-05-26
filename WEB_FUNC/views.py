from django.shortcuts import render


# Create your views here.
def mandybirthday(request):
    return render(request, 'mandybirthday2019.html')


def love2019520(request):
    return render(request, '2019520.html')
