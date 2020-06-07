from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     required=True,
    #     attrs={
    #         "placeholder": "Title"
    #     }
    # )
    # content = forms.Textarea(
    #     required=True,
    #     attrs={
    #         "id": "text_area_post",
    #         "rows": 20,
    #         "cols": 120
    #     }
    # )
    # active = forms.BooleanField(
    #     required=True,
    # )

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]