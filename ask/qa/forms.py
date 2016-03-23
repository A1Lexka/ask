form django import forms


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        text = self.cleaned_data['text']
        if not form.is_valid(text):
            raise forms.ValidationError('text is wrong', code=12)
        return text + "Thank you."

    def save(self):
        text = Question(**self.cleaned_data)
        text.save()
        return text


class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100)
    question = forms.IntegerField()

    def clean(self):
            
    















