from django.shortcuts import render

# Create your views here.
def fun(request):
    return render(request,"index.html")



def cookiecount(request):
    count = request.COOKIES.get('count', '0')  # Default value '4' as a string
    try:
        total_count = int(count) + 1
    except ValueError:
        total_count = 5  # Default value in case of conversion failure
    
    response = render(request, "cook.html", {'count': total_count})
    response.set_cookie('count', total_count)  # Set the updated count in the cookie
    return response

