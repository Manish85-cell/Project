from sys import executable
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, CodeSubmission
import os
import uuid
from pathlib import Path
import subprocess
from django.conf import settings
def index(request):
    return render(request , "oj/index.html")

LANGUAGE_CHOICES = [
    ("py", "Python"),
    ("c", "C"),
    ("cpp", "C++")
]




       

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "oj/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "oj/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "oj/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "oj/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "oj/register.html")
    
    
def editor(request):
    return render(request, "oj/editor.html")

def run_code(language, code, input_data):   
    project_path = Path(settings.BASE_DIR)
    directories = ["codes", "input", "outputs"]
    
    for directory in directories:
        dir_path = project_path/directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok = True)
    
    codes_dir = project_path / "codes"
    input_dir = project_path / "input"
    output_dir = project_path / "outputs"
    
    unique = str(uuid.uuid4())
    
    code_file_name = f"{unique}.{language}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"
    
    code_file_path = codes_dir / code_file_name
    input_file_path = input_dir / input_file_name
    output_file_path = output_dir / output_file_name


    with open(code_file_path, "w") as code_file:
        code_file.write(code)
    
    with open(input_file_path, "w") as input_file:
        input_file.write(input_data) 
    with open(output_file_path , "w") as output_file:
         pass    
    if language == "cpp":
        executable_path = codes_dir / unique
        compilation_command = f"g++ {str(code_file_path)} -o {str(executable_path)} -lstdc++"
        os.system(compilation_command)
        compile_result = subprocess.run(
            ["g++",str(code_file_path), "-o", str(executable_path), "-lstdc++"],
            check=True
        )
        if compile_result.returncode == 0:
            subprocess.run(["chmod", "+x", str(executable_path)])
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    subprocess.run(
                        [str(executable_path)],
                        stdin = input_file,
                        stdout = output_file
                    )
    elif language == "py":
        with open(input_file_path, "r") as input_file:
            with open(output_file_path , "w") as output_file:
                subprocess.run(
                    ["python", str(code_file_path)],
                    stdin = input_file,
                    stdout = output_file
                ) 
    
 
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()
        
    return output_data
                  
     
class CodeSubmissionFORM(forms.ModelForm):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    
    class Meta:
        model = CodeSubmission
        fields = ["language", "code", "input_data"]            
     
def submit(request):
    if  request.method == "POST":
        form = CodeSubmissionFORM(request.POST)
        if form.is_valid():
            submission = form.save()
            print(submission.language)
            print(submission.code)
            output = run_code(
                submission.language, submission.code, submission.input_data
            )
            submission.output_data = output
            submission.save()
            return render(request,"oj/result.html", {"submission": submission})
    form = CodeSubmissionFORM()
    context = {
        "form": form,
    }
    return render(request, "oj/compiler.html", context)


            
 
    