from django.shortcuts import render

# Create your views here.

def main_view(request):
    """_summary_: This is the main view for the portfolio app.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: home temaplate
    """
    return render(request, 'home.html')

def template_view(request):
    return render(request, 'templates.html')

def project_view(request):
    """_summary_: This is the  view for the each project.

    Args:
        request (_type_): HttpRequest

    Returns:
        _type_: _description_
    """
    return render(request, '')