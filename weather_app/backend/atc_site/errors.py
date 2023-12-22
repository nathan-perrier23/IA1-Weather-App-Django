from django.shortcuts import render

def handler400(request, exception):
    context = {'title': 'Bad Request', 'error': '400', 'desc': 'There was an issue processing your request. This could be due to an invalid action or input. Please try again or return home.'}
    return render(request, 'atc_site//error.html', context, status=400)

def handler404(request, exception):
    context = {'title': 'Page Not Found', 'error': '404', 'desc': 'We’re sorry, the page you have looked for does not exist in our website! Maybe go back to our home page or user the navigation bar?'}
    return render(request, 'atc_site//error.html', context, status=404)

def handler500(request):
    context = {'title': 'Internal Server Error', 'error': '500', 'desc': 'There is an error in loading the sever. Plase try again later.'}
    return render(request, 'atc_site//error.html', context, status=500)

def handler401(request, exception):
    context = {'title': 'Unauthorized', 'error': '401', 'desc': 'You are not authorized to view this page. Please try again or return home.'}
    return render(request, 'atc_site//error.html', context, status=401)

def handler403(request, exception):
    context = {'title': 'Forbidden', 'error': '403', 'desc': 'You are not allowed to view this page. Please try again or return home.'}
    return render(request, 'atc_site//error.html', context, status=403)