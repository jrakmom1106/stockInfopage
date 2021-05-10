from django.contrib import admin
from .models import Book

# 어플리케이션마다 admin이 있다.
from .models import Question


admin.site.register(Question)


admin.site.register(Book)