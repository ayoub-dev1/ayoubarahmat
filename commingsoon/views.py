from django.shortcuts import render

def home(request):
	
	context = {
		'facebook':'https://www.facebook.com/ayoubarahmat',
		'twitter': 'https://twitter.com/AyoubArahmat',
		'instagram': 'https://www.instagram.com/ayoub_vibes/',
		'linkedin':'https://www.linkedin.com/in/ayoubarahmat/'
	}
	return render(request, 'commingsoon/index.html',context)