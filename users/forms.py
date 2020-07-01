from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("올바른 비밀번호가 아닙니다"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("존재하지 않는 사용자 입니다"))

        # print("clean_password")
