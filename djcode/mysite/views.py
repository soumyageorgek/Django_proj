from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def search_form(request):
    return render_to_response('search_form.html')

def contact(request):
    import os
    errors = []
    if request.method == 'POST':
        print 'jklmno'
	os.system('rm resume.*')
        resum = request.POST.get('message', '')
        f = open('resume.tex', 'w')
        f.write(resum)
        f.close()
        os.system('yes "" | pdflatex resume.tex')
        response = HttpResponse(mimetype="application/pdf") 
        response['Content-Disposition'] = 'attachment; filename=resume.pdf'
        f = open('resume.pdf', 'r');
        response.write(f.read())
        f.close()
        #send_mail(request.POST['subject'], request.POST['message'], request.POST.get('email', 'noreply@example.com'), ['siteowner@example.com'],)
        return response #HttpResponse('post worked successfully')
		
            #return HttpResponseRedirect('/contact/thanks/')
