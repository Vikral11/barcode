from django.shortcuts import render
import pyqrcode

# Create your views here.


def home(request):
    if (request.method=="POST"):
        bar=request.POST.get("bartext")
        print(bar)
        s=pyqrcode.create(bar)
        y=s.png_as_base64_str(scale=5)

        return render(request,"download.html",{"x":y})
        
    return render(request,"index.html")



