from re import template
from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.http import HttpResponse
import textwrap


class IndexView(View):

    def get(self, request, *args, **kwargs):
        subject = "【あしあと】配布したQRコードから貴社サイトにアクセスがありました"
        message = request.build_absolute_uri()
        from_email = "web.knakasaka@gmail.com"
        recipient_list = ["web.decube@gmail.com"]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse('無効なヘッダが検出されました。')
        return render(request, 'sendmail/redirect.html')
    template_name = 'index.html'

class RedirectView(View):
    template_name = 'redirect.html'
    
