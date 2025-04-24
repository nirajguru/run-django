## Niraj notes: This file is a Django view that handles the logic for a web application. It includes functions to display a form, process the form submission, and display the results. The form allows users to enter their name and phone number, and the results are displayed on a separate page. The code also includes error handling for invalid input.
## it might call models.py that interacts with the database and might use templates to provide the response to the user


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey you are at index page.")

def about(request):
    return HttpResponse("Hey you are at about page.")
