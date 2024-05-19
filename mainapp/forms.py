from django import forms


class Contact(forms.Form):
    name = forms.CharField("Enter your Name", max_length=50, required=True)
    # email = forms.EmailField("Your Email (So I can revert back to you)", required=True)
    suggestion = forms.Textarea("Your suggestion")
