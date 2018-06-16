from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.views.generic.base import View
from django.db import connection
# Create your views here.

# cur = connection.cursor()  
#         # execute the stored procedure passing in
#         # search_string as a parameter
#         cur.callproc('searcher_document_search', [search_string,])
#         # grab the results
#         results = cur.fetchall()
#         cur.close()
#
#         # wrap the results up into Document domain objects
#         return [Document(*row) for row in results]

@login_required
def start(request):
    current_user = request.user
    return render(request, 'main_page.html', locals())

@login_required
def added(request):
    current_user = request.user
    return render(request, 'added.html', locals())

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login/")
