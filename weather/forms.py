from django import forms

class weatherForm(forms.Form):

	city = forms.CharField()

	class Meta:
		fields = ('city')