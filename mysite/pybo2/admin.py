# Django 관리자 기능을 사용하기 위해 불러옴
from django.contrib import admin

# 현재 앱의 Question 모델을 불러옴
from .models import Question

# 관리자 페이지에서 검색 기능 설정
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']   # 'subject' 필드로 검색할 수 있게 만듦

# Question 모델을 관리자 페이지에 추가
admin.site.register(Question, QuestionAdmin)