from django.shortcuts import render

def about_view(request):
    return render(request, "about.html", {})

def err_404_handler(request):
    return render(request, "err_handler.html", {"err_msg":"Page not found !"})

def err_500_handler(request):
    return render(request, "err_handler.html", 
                    {"err_msg":"We are facing internal error :/"}
                )
