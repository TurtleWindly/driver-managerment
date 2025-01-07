from django import forms

from .models import Course, License, DriverLicense


class CourseForm(forms.ModelForm):
    def clean_license_fk(self):
        return License.objects.get(id=self.data["license_fk"])

    class Meta:
        model = Course
        fields = [
            "name",
            "teachers",
            "exam_date",
            "graduation_date",
            "license_fk",
        ]
