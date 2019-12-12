from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,'frontend/index.html')


# def footer(request):
#     return render(request,'frontend/footer.html')