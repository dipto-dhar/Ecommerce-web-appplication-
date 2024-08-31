from django.http import HttpResponse
from django.shortcuts import redirect



def authenticated_user(allowed_roles=[]):
    def authenticator(func):
        def wrapper(request, *args,**kwargs):
            print(allowed_roles[0])
            print(request.user.groups)
            if request.user.is_authenticated:
                if request.user.groups.name in allowed_roles:
                    return func(request,*args,**kwargs)
                else:
                    return HttpResponse("you are not authorized")
            else:
                return redirect('login')
        return wrapper
    return authenticator
            