from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView

from weather.forms import CoordinateForm
from weather.services import WeatherService


class WeatherView(View):
    service = WeatherService

    def get(self, request):
        form = CoordinateForm()
        return render(request, 'index.html', context={"form": form})

    def post(self, request):
        form = CoordinateForm(request.POST)

        if form.is_valid():
            lat = form.cleaned_data['latitude']
            lon = form.cleaned_data['longitude']

            weather = self.service.get_weather_info(lat, lon)

            return render(request, 'weather.html', context={"weather": weather})

        return render(request, 'index.html', context={"form": form})
