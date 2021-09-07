from django.shortcuts import render

# Create your views here.
def book_now(request):
    if request.GET:
        print("request was GET!")

    return render(request, 'book-now.html')

def show_available_times(request):

    

    print(request)

    return render(request, 'available-times.html')