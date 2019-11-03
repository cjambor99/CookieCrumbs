from django.shortcuts import redirect

def handler404(request, exception):
    # make a redirect to homepage
    return redirect('/cookieCrumbs')