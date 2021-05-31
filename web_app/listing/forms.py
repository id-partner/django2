from django import forms


class ReviewForm(forms.Form):
    head = forms.CharField(min_length=4, max_length=250)
    name = forms.CharField(min_length=4, max_length=20)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea, max_length=1500, min_length=20)
    rating = forms.FloatField()
    positive = forms.CharField(widget=forms.Textarea, max_length=500, min_length=5, required=False)
    negative = forms.CharField(widget=forms.Textarea, max_length=500, min_length=5, required=False)
