from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from .forms import UserRegistrationForm,UserSignInForm
from .models import MyUser
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class UserSignUpView(CreateView):
    template_name = "register.html"
    form_class = UserRegistrationForm
    model = MyUser
    success_url = reverse_lazy("signup")

class UserSignInView(TemplateView):
    template_name="login.html"
    form_class=UserSignInForm
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["form"]=self.form_class
        return context
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                if user.role=="ADMIN":
                    return render(request, "home.html")
                elif user.role=="MANAGER":
                    return render(request, "homemanag.html")
                elif user.role == "HR":
                    return render(request,"Hrhome.html")
            return redirect('signin')