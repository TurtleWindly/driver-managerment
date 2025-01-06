from django.db import models


class CourseTemplate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tên mẫu")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mẫu khóa học"
        verbose_name_plural = "Các mẫu khóa học"


class LessonTemplate(models.Model):
    course = models.ForeignKey(
        CourseTemplate, on_delete=models.CASCADE, verbose_name="Mẫu khóa học"
    )
    name = models.CharField(max_length=255, verbose_name="Tên mẫu bài học")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mẫu bài học"
        verbose_name_plural = "Các mẫu bài học"
