from django.shortcuts import render
from school import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.base import TemplateView


class PaymentSuccessView(View):
    template_name = 'payments/payments_success.html'

    def get(self, request):
        return render(request, self.template_name)


class PaymentFailedView(View):
    template_name = 'payments/payments_failed.html'

    def get(self, request):
        return render(request, self.template_name)


class PaymentsView(TemplateView):
    template_name = 'payments/payments.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
