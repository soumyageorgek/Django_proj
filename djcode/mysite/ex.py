from django.http import HttpResponse
def some_view(request):
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=resume.pdf'
	f = open(resume.pdf, 'r');
	response.write(f)
	f.close()
	


