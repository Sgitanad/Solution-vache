from django.shortcuts import render

def main(request):
    return render(request, 'blog/main.html', {})

def next(request):
    return render(request, 'blog/next.html', {})
