from django.shortcuts import render, get_object_or_404
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import sessions
from django.contrib.auth.decorators import login_required
# Create your views here.
Language = [
    {'value':'py' ,'label': 'python'},
    {'value':'cpp', 'label':'cpp'},
    {'value':'c', 'label':'c'}
]

def index(request):
    message = ""
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.method == "POST":
        task = request.POST["task"]
        username = request.POST["username"]     
        if username != "":
           request.session["tasks"].append(task)
           request.session.save()
        else:
            message = "Login required"
    return render(request, "oj/index.html",{
        "tasks":request.session["tasks"], "message":message
    })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        
        password = request.POST["password"]
        confirm = request.POST["confirmation"]
        if confirm != password:
            return render(request, "oj/register.html", {username : "username" , "message":"Password not matches"})
        
        #Attempt to create a user
        try:
           user = User.objects.create_user(username, email, password)
           user.save()
        except IntegrityError:
            return render(request, "oj/register.html", {"message":"username already taken"})
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "oj/register.html")        
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username = username , password = password)
        
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        return render(request, "oj/login.html", {"message":"Invalid Details"})
    return render(request, "oj/login.html", {"messages":""})     

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

from pathlib import Path
import uuid
import subprocess
def run_code(code, lang, input_data):
    project_path = Path(settings.BASE_DIR)
    directories = ["code", "input", "output"]
    
    for directory in directories:
        dir_path = project_path/directory
        dir_path.mkdir(parents=True, exist_ok=True)
    
    codes_dir = project_path / "code"
    input_dir = project_path / "input"
    output_dir = project_path / "output"
    
    unique = str(uuid.uuid4())
    
    code_file_path  = codes_dir / f"{unique}.{lang}"
    input_file_path = input_dir / f"{unique}.txt"
    output_file_path = output_dir / f"{unique}.txt"
    
    try:
        with open(code_file_path, "w") as code_file:
            code_file.write(code)
        with open(input_file_path, "w") as input_file:
            input_file.write(input_data)
            
        #creating empty output file
        output_file_path.touch()
        
        if lang == "cpp" or lang == "c":
            executable_path = codes_dir / (unique + ".exe")
            compilation_command = ["g++", str(code_file_path), "-o", str(executable_path)]
            compile_result = subprocess.run(
                compilation_command,
                stderr = subprocess.PIPE,
                text = True
            )
            if compile_result.returncode != 0:
                return compile_result.stderr
            run_command = [str(executable_path)]
        elif lang == "py":
            run_command = ["python", str(code_file_path)]
        else:
           return "Unsupported language"
        run_result = subprocess.run(
            run_command,
            stdin = open(input_file_path, "r"),
            stdout = open(output_file_path, "w"),
            stderr = subprocess.PIPE,
            text = True
        )
        
        if run_result.returncode != 0:
            return run_result.stderr
        
        with open(output_file_path, "r") as output_file:
            output_data = output_file.read()
        
        return output_data
    except Exception as e:
        return str(e)
             
         
# def submit(request):
#     curr_code = ""
#     curr_lang = "cpp"
#     curr_input = ""
#     if request.method == "POST":
#         code = request.POST["code"]
#         lang = request.POST["language"]
#         input_data = request.POST["input_data"]
#         curr_code = code
#         curr_lang = lang
#         curr_input = input_data
#         output = run_code(code, lang, input_data)        
#         return render(request, "oj/editor.html", {"submission":output, "options":Language, "code" : curr_code, "lang": curr_lang, "input": curr_input})
#     return render(request, "oj/editor.html", {"options":Language, "code" : curr_code, "lang": curr_lang, "input": curr_input})  




from .models import Testcase, Problems

def problems(request):
    problems = Problems.objects.all()
    if "status" not in request.session:
        request.session["status"] = False
    status = request.session["status"]
    if request.method == "POST":
        name = request.POST["q"]
        name = name.lower()
        print(name)
        recommendation = []
        for prob in problems:
            p = (prob.name).lower()
            if name in p:
                recommendation.append(prob)
            print(p)
            print(name)
        return render(request, 'oj/problems.html', {"Problems":recommendation})
    return render(request, 'oj/problems.html', {'Problems':problems, 'status':status})



@login_required
def submit(request, problem, Testcases):
    code = request.POST["code"]
    lang = request.POST["language"]
    curr_code = code
    curr_lang = lang
    i = 1
    message = ""
    for Testcase in Testcases:
        input_data = Testcase.input_data      
        output_data = Testcase.output_data      
        
        output = run_code(code, lang, input_data)
        # print(f"{output}== {output_data}")
        # print(output)
        if output != output_data:
            message = f"Failed on Test Case {i}"
            return render(request, 'oj/solve.html', {"problem":problem, "options":Language, "lang":curr_lang, "code": curr_code, "input":input_data, "message":message, "output":output, "expected_output":output_data})
        i+=1
    message = f"All {i} Testcases Passed"
    
    request.session["status"] = True
    
    return render(request, 'oj/solve.html', {"problem": problem, "options": Language, "lang":curr_lang, "code":curr_code, "message":message})

def solve(request, problem_id):
    problem = get_object_or_404(Problems, id=problem_id)
    if "status" not in request.session:
        request.session["status"] = False 
    status = request.session["status"]
 
    
    Testcases = problem.test_cases.all()
    curr_code = ""
    curr_lang = "cpp"
    curr_input = ""
    if request.method == "POST":
        if request.POST.get('action') == 'run':
            code = request.POST["code"]
            lang = request.POST["language"]
            input_data = request.POST["input_data"]
            curr_code = code
            curr_lang = lang
            curr_input = input_data
            output = run_code(code, lang, input_data)
            print(output)
            return render(request, "oj/solve.html", {"problem":problem ,"output":output, "options":Language, "code" : curr_code, "lang": curr_lang, "input": curr_input})       
        return submit(request, problem, Testcases)
    return render(request, 'oj/solve.html', {"problem" : problem, "options":Language, "status":status})