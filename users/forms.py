from django import forms
from . import models
from django.contrib.auth import password_validation


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


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password1 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="이전과 동일한 비밀번호를 입력하세요.",
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("해당 이메일은 존재하는 이메일입니다")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")
        else:
            try:
                password_validation.validate_password(password1, self.instance)
                return password
            except forms.ValidationError as error:
                self.add_error("password", error)

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()
