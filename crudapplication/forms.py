from django import forms
from crudapplication.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # ("eid","ename",)
        fields = "__all__"


        