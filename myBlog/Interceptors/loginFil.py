from django.shortcuts import HttpResponseRedirect

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.safeList = ['/index/toLogin','/index/logined','/index/','/index/registerIt','/index/RegisterUser','/index/checkRegister']
    def process_request(self, request):
        print(request.get_full_path())
        print(request.path)
        print("login? -->", request.session.get('haslogin', False))
        print("request path is ", request.path)



        if request.session.get('haslogin', False) == False and request.path not in self.safeList :
            return HttpResponseRedirect('/index/toLogin')
        else:
            print("here-->",request.get_full_path())

            # if request.get_full_path() == '/':
            #     return HttpResponseRedirect('/index')
            # else:
            #     return HttpResponseRedirect(request.get_full_path())
