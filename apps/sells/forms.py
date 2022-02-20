from django.core import validators
from django import forms
from django.forms import widgets
from .models import Sells
from django.core.mail import send_mail

class SellsForm(forms.ModelForm):
    class Meta:
        model = Sells
        fields = [
            'item', 
            'company', 
            'frc',
            'item_qty', 
            'price', 
            'comment'
        ]
        # widgets = {'user_name': forms.HiddenInput()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_qty'].widget.attrs['min'] = "1"
        self.fields['item_qty'].widget.attrs['max'] = "5"
    
    # def funn(self, user_name):
        
    # # def send_email(self, user_name):
    # #     send_feedback_email_task.delay()
    #     # print(self.cleaned_data)
    #     # # send email using the self.cleaned_data dictionary
    #     name = "NP Online"#request.POST.get('name')
    #     subject = "NP Online " + user_name
    #     message = str(self.cleaned_data['item_qty']) + ' ' + str(self.cleaned_data['item_name'].item_name) + " sold by " + user_name + " with price of " + str(self.cleaned_data['price']) + "\n" + str(self.cleaned_data['comment'])
    #     # fun.delay(name, subject, message)
    #     # print(name, subject, message)

    #     # send_mail(
    #     #     subject,
    #     #     message,
    #     #     'popatnirmal2233@gmail.com',
    #     #     ['popatnirmal2233@gmail.com', 'tejalpopat735@gmail.com', 'harshmangvani89@gmail.com'],
    #     #     fail_silently=False,
    #     # )
        
    #     '''stocks =[]
    # count = 0
    # for i in Stock.objects.all():
    #     stocks.append([count, i.item_name])
    #     count += 1
    # stocks = tuple(stocks)
    # print(stocks)
    # item_name = forms.ChoiceField(choices = stocks, widget = forms.RadioSelect)'''