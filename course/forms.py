from django import forms

from .models import Course, License


class CourseForm(forms.ModelForm):

    def clean_license_fk(self):
        return License.objects.get(id=self.data["license_fk"])

    def clean_students(self):
        course_license = self.clean_license_fk()
        students = self.cleaned_data.get("students", None)
        for student in students:
            if student.license_fk != course_license:
                self.add_error(
                    "students",
                    f"user {student.user} đăng ký bằng lái {student.license_fk}",
                )
        return students

    class Meta:
        model = Course
        fields = [
            "name",
            "teachers",
            "students",
            "exam_date",
            "graduation_date",
            "license_fk",
        ]
