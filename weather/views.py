from django.shortcuts import render_to_response, render
from .forms import weatherForm
import urllib2
import json



API_ID = 'eb7a80fcd78240da4fffdb5b8534a47f'


def temperature(request):
	form = weatherForm
	print form
	return render(request, 'temperature.html', {'form': form})

def results(request):
	appid = API_ID

	if request.POST:
		form = weatherForm(request.POST)
		city = request.POST.get('city')
		
		if form.is_valid():
			url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=' + appid

			json_obj = urllib2.urlopen(url)
			data = json.load(json_obj)

			print data["main"]["temp"] - 273

			return render(request, 'temperature.html', {'temp': data["main"]["temp"] - 273, 'city': city})


# city = raw_input("ENTER THE NAME OF THE CITY:  ")