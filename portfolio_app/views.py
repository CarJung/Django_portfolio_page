from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.

def main_view(request):
    """_summary_: This is the main view for the portfolio app.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: home temaplate
    """
    return render(request, 'index.html')

def cv_view(request):
    try:
        return FileResponse(open('CV Krzysztof Wróbel.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def Diabetes_view(request):
    """_summary_: This is the  view for the each project.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: _description_
    """
    return render(request, 'Diabetes.html')

def Seizure_view(request):
    """_summary_: This is the  view for the each project.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: _description_
    """
    return render(request, 'Seizure.html')

def Stat_app_view(request):
    """_summary_: This is the  view for the each project.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: _description_
    """
    return render(request, 'Stat_test_app.html')

def Estates_view(request):
    """_summary_: This is the  view for the each project.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: _description_
    """
    return render(request, 'Estates.html')

def data_camp_view(request):
    """_summary_: This is the  view for the each project.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: _description_
    """
    return render(request, 'Data_camp.html')