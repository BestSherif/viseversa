from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def reverse(request):
    user_text = request.GET['usertext']
    count_string = user_text.split()
    number_of_words = len(count_string)
    reversed_text = user_text[::-1]
    return render(request,'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'numberofwords': number_of_words})