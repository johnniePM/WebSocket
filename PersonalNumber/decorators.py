import functools
from django.shortcuts import redirect
from django.contrib import messages
from .models import Mobile_user
from KasaRegister.models import KasaUser
from django.contrib.sessions.models import Session
from django.http import HttpRequest
import json

    
def mobile_is_authenticated(view_func, redirect_url="prn:mobile_login"):
    """
        this decorator ensures that a pc user is logged in,
        if a pc user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(request:HttpRequest, *args, **kwargs):
        try:
          print("request.session")
          post_mobileIdentifier=request.session["personal_number"]
          print(request.session["personal_number"])
          print(post_mobileIdentifier)
          print("request.session")
          pc=Mobile_user.objects.get(personal_number=post_mobileIdentifier)
          if "receiver" in request.session:
            receiver=request.session["receiver"]
            receiver=json.loads(receiver)
            try:
              print(receiver)
              for item in receiver:
                print(item)
                kasa_user=KasaUser.objects.get(username=item)
                print("kasa_user.username")
                print(kasa_user.username)
                print("kasa_user.username")
              return view_func(request,*args, **kwargs)
            except Exception as e:
               print("_______________________except____________________________")
               print(e)
               print("_______________________except____________________________")
               return redirect("prn:choose_kasa")
          else:
            print("_______________________else____________________________")
            print(e)
            print("_______________________else____________________________")
            return redirect("prn:choose_kasa")
             
        except Exception as e:
          print(e)
          messages.info(request, "You need to be logged in")
          return redirect(redirect_url)
    return wrapper