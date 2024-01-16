from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Congratulations, We have deployed successfully to AKS using Azure Pipelines!")
# Create your views here.
