from django.urls import path,re_path, register_converter
from . import views

# 정규 표현식을 이용해서 url구성 방법
class YearConverter:
    regex = r"20\d{2}"

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return "%04d" % value

# Converter 설정
register_converter(YearConverter, 'year')

app_name = 'instagram' # URL Reverse에서 namespace 역활을 하게 됩니다.

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('<int:pk>/',views.post_detail),
    # path('archives/<int:year>/',views.archives_year),
    # path(r'archives/(?P<year>20\d{2})/',views.archives_year), # 쿼리 파람값을 20~~ 로 받기
    path('archives/<year:year>/',views.archives_year), # Converter 정의
]
