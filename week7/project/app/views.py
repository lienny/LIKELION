from django.shortcuts import render

# Create your views here.
def count(request):
    text = request.POST['text']
    no_blank_len = len(text.replace(" ",""))
    total_len = len(text)
    word_count = len(text.split()) 
    return render(request, 'count.html', {
        'total_len' : total_len,
        'text' : text,
        'no_blank_len' : no_blank_len,
        'word_count' : word_count
    })