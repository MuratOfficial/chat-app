from django.shortcuts import render, redirect

# Create your views here.

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    return render(request, 'chat/chatPage.html', context)

