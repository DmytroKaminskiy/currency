import csv

from django.http import HttpResponse
from django.views.generic import ListView, View, TemplateView

from rate.models import Rate
from rate.selectors import get_latest_rates
from rate.utils import display


class RateList(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate-list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['hello'] = 'world'
    #     return context


class LatestRatesView(TemplateView):
    template_name = 'latest-rates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_latest_rates()
        return context


class RateDownloadCSV(View):
    HEADERS = (
        'id',
        'created',
        'source',
        'amount',
        'type',
    )
    queryset = Rate.objects.all().iterator()

    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = self.get_response()

        writer = csv.writer(response)
        writer.writerow(self.__class__.HEADERS)

        for rate in self.queryset:
            values = []
            for attr in self.__class__.HEADERS:
                values.append(display(rate, attr))

            writer.writerow(values)

        return response

    def get_response(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="rate.csv"'
        return response
