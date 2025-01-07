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


class DriverLicenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["is_qualified"].widget.attrs["disabled"] = True
        self.fields["is_graduation"].widget.attrs["disabled"] = True

    def clean_course(self):
        license_fk = self.cleaned_data["license_fk"]
        course = self.cleaned_data["course"]
        if license_fk != course.license_fk:
            self.add_error("course", f"Khóa học này có bằng loại {course.license_fk}")
        return course

    class Meta:
        model = DriverLicense
        fields = [
            "user",
            "license_fk",
            "course",
            "is_active",
            "theory_ok",
            "practice_ok",
            "is_qualified",
            "is_graduation",
            "tuition",
            "tuition_paid",
            "exam_tuition",
            "exam_tuition_paid",
            "exam_tuition_note",
            "a1_note",
            "note",
        ]
