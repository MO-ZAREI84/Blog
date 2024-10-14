from django import forms
from .models import Comment

class TicketForm(forms.Form):
    # SUBJECT_CHOICES = (
    #     ('پیشنهاد', 'پیشنهاد'),
    #     ('انتقاد', 'انتقاد'),
    #     ('گزارش', 'گزارش'),
    # )
    message=forms.CharField(widget=forms.Textarea,required=True)
    name=forms.CharField(max_length=250,required=True)
    email=forms.EmailField()
    phone=forms.IntegerField(required=True)
    subjects = forms.ChoiceField(
        label="موضوع",
        choices=[
            ('پیشنهادات', 'پیشنهادات'),
            ('انتقادات', 'انتقادات'),
            ('گزارش', 'گزارش')
        ],
        required=True
    )
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','body']