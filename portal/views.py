from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from . models import Complaint
from .models import CustomUser


# Home View - All Complaints Tab - Shows All the complaints in the DB
def home(request):
    # return render(request, 'portal/home.html')
    items = Complaint.objects.all()
    return render(request, 'home.html', {'complaints': items})

def signup(request):
    return render(request, 'signup.html')

# End-point for saving new complaints 
def complaint(request):
    if request.method == 'POST':
        title = request.POST['title']
        discription = request.POST['discription']
        faculty = request.POST['faculty']
        date = request.POST['date']
        status = "Pending"

        NewComplaint = Complaint(
            title=title, discription=discription, status=status, faculty=faculty, pub_date=date)
        NewComplaint.save()

        #print(title, discription, faculty, date)
    return render(request, 'complaint.html')

def submit_complaint(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        discription = request.POST.get('discription')
        faculty = request.POST.get('faculty')
        date = request.POST.get('date')
        status = "Pending"

        NewComplaint = Complaint(
            title=title, discription=discription, status=status, faculty=faculty, pub_date=date)
        NewComplaint.save()
        # Validate the data (add your validation logic here)
        

        # Send email to admin
        subject = f'New Complaint: {title}'
        message = f'Title: {title}\nDescription: {discription}\nFaculty: {faculty}\nDate: {date}'
        from_email = 'settings.EMAIL_HOST_USER'  # Replace with your email
        to_email = 'desdad9@gmail.com'  # Replace with the admin's email

        send_mail(subject, message, from_email, [to_email])
        
    return render(request, 'success_page.html')  # Replace with the actual template name


# Protected View - For Staff to see the complains assigned to them
def staff(request):
    # Check for session
    user_id = request.session.get('user_id')
    if user_id:
        # User is authenticated;
        # user = CustomUser.objects.get(username=user_id)
        # print(user_id)

        # get all complains for current logged in member
        items = Complaint.objects.filter(faculty=user_id).values()
        return render(request, 'staff.html', {'complaints': items})

    else:
        # User is not authenticated; redirecting to the login page
        return redirect('login')


# End-point to change status of a complaint
def resolve_complaint(request, complaint_id):
    # Get the complaint object to delete or return a 404 error if not found
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)

    if request.method == 'POST':
        # Toggle the complaint staus
        if complaint.status == "Resolved":
            complaint.status = "Pending"
        else:
            complaint.status = "Resolved"
        complaint.save()

        # Redirect to a page after successful updation 
    return redirect('staff')


# End=point for delete session and logout
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')  

# Login View - Auth End-point
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        try:
            user = CustomUser.objects.get(username=username)
            print(user)
            if user.check_password(password):
                # Authentication successful
                # Set a session variable
                # create a session for the user
                request.session['user_id'] = user.username
                return redirect('staff')
            else:
                # Authentication failed
                return render(request, 'login.html')
        except CustomUser.DoesNotExist:
            # Username not found
            return render(request, 'login.html')
    return render(request, 'login.html')

def help_view(request):
    return render(request, 'help.html')

def about_view(request):
    return render(request, 'about.html')

def report_issue_view(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        description = request.POST['description']

        send_mail(
            subject,
            description,
            'desdad9@gmail.com',
            ['desmond.dadzie@stu.ucc.edu.gh'],
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('success_page'))

    return render(request, 'report.html')

def success_page(request):
    return render(request, 'success_page.html')