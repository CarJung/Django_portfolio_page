from django.shortcuts import render

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
    """_summary_: This is the  view for the each project.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: _description_
    """
    return render(request, 'CV.html')

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
    return render(request, 'Stat_app.html')

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