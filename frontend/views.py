from django.shortcuts import render

# Create your views here.
def test(request):
    # print("HIIIIIII")
    # if request.method == 'POST':
    #     print("HIIIIIII")
    #     postdata = request.post.copy()
    #     print("HIIIIIII")
    return render(request,'frontend/index.html')


# def footer(request):
#     return render(request,'frontend/footer.html')
