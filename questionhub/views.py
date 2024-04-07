from django.http import HttpResponse

def robotstxt(request):
    return HttpResponse('''User-agent: *\nDisallow: ''', headers = {
            "content-type":"text/plain"
        }
    )
