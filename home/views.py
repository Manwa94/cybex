from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
# from blog.models import Post

# Create your views here.
def home(request): 
    return render(request,'home/home.html')
    #return HttpResponse('This is home ')

def contact(request):
    return render(request,'home/contact.html')

def company(request): 
    return render(request,'home/company.html')
    #return HttpResponse('This is Feedback')

def service(request): 
    return render(request,'home/service.html')
    #return HttpResponse('This is Feedback')

def technology(request): 
    return render(request,'home/technology.html')
    #return HttpResponse('This is Feedback')

# def search(request):
#     query=request.GET['query']
#     if len(query)>78:
#         allPosts=Post.objects.none()
#     else:
#         allPostsTitle= Post.objects.filter(title__icontains=query)
#         allPostsAuthor= Post.objects.filter(author__icontains=query)
#         allPostsContent =Post.objects.filter(content__icontains=query)
#         allPosts=allPostsTitle.union(allPostsContent, allPostsAuthor)
#     if allPosts.count()==0:
#         messages.warning(request, "No search results found. Please refine your query.")
#     params={'allPosts': allPosts, 'query': query}
#     return render(request, 'home/search.html', params)

#Authentication pages
# def handleSignUp(request):
#     if request.method=="POST":
#         # Get the post parameters
#         username=request.POST['username']
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#         email=request.POST['email']
#         pass1=request.POST['pass1']
#         pass2=request.POST['pass2']

#         # check for errorneous input
#         if len(username)<10:
#             messages.error(request, " Your user name must be under 10 characters")
#             return redirect('home')

#         if not username.isalnum():
#             messages.error(request, " User name should only contain letters and numbers")
#             return redirect('home')
#         if (pass1!= pass2):
#              messages.error(request, " Passwords do not match")
#              return redirect('home')

        
#         # Create the user
#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name= fname
#         myuser.last_name= lname
#         myuser.save()
#         messages.success(request, " Your Profile has been successfully created")
#         return redirect('home')

#     else:
#         return HttpResponse("404 - Not found")


# def handeLogin(request):
#     if request.method=="POST":
#         # Get the post parameters
#         loginusername=request.POST['loginusername']
#         loginpassword=request.POST['loginpassword']

#         user=authenticate(username= loginusername, password= loginpassword)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("home")
#         else:
#             messages.error(request, "Invalid credentials! Please try again")
#             return redirect("home")

#     return HttpResponse("404- Not found")
   

#     return HttpResponse("login")

# def handelLogout(request):
#     logout(request)
#     messages.success(request, "Successfully logged out")
#     return redirect('home')

