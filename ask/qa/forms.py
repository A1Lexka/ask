form django import forms


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

#    def check_form(www):
#        if 'XXX' in www:
#            return False
#        else:
#            return True 
#
#

    def clean(self):
        text = self.cleaned_data['text']
        if not text.is_valid():
            raise forms.ValidationError('question text is wrong', code=12)
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100)
    question = forms.IntegerField()

    def clean(self):
        text = self.cleaned_data['text']
        if not text.is_valid():
            raise forms.ValidationError('answer text is wrong', code=11)    
        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer




  
   














