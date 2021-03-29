from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(min_length=4, max_length=20)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea, max_length=1500, min_length=20)
    rating = forms.FloatField()
