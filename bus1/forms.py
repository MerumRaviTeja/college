from django import forms
from .models import faculty,studentfake,student
class facultyform(forms.ModelForm):
    class Meta:
        model=faculty
        fields=['faculty_name','subject','department','qualification','experience','email']
        
class studentform(forms.ModelForm):
    class Meta:
         model=student
         fields = ['student_name','branch','year','email']
class facultyloginform(forms.ModelForm):
    class Meta:
         model=faculty
         fields = ['subject','email']
class studentloginform(forms.ModelForm):
    class Meta:
         model=studentfake
         fields = ['student_ID','branch']
