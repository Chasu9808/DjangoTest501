from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger


# views - controller 역할.

# 터미널에서, 단위 테스트 연습해보기.
# python
# 입력 후, 모양이 >>>
# from burgers.models import Burger
# 오류 발생하면,
# 다시 터미널에서, ctrl + z
# python manage.py shell
# from burgers.models import Burger
# Burger

# 해당 모델 객체의 목록 모두 가져오기.
# Burger.objects.all()

# 하나 가져오기
# Burger.objects.get(name="불고기버거")
# 임시 변수에 담아서, 객체 형식으로 확인.
# burger = Burger.objects.get(name="불고기버거")
# 객체의 각 필드요소를 조회.
# burger.id
# burger.name
# burger.price
# burger.calories

# 조건으로 , 모델에서, 해당 객체 조회. 끝나는 이름으로 조회.
# burgers = Burger.objects.filter(name__endswith="버거")
# type(burgers)
# <class 'django.db.models.query.QuerySet'>

# len(burgers)
# 3
# >>> burgers[1]
# <Burger: 불고기버거>

# 반복문으로, 목록 요소의 내용 조회하기.
# for burger in burgers:
#     print(burger.id, burger.name, burger.price, burger.calories)





def main(request):
    # 단순 문자열만 리턴,
    # return HttpResponse("Hello, world.")
    # 화면을 연결해서 응답하기.
    return render(request, 'main.html')


def main2(request):
    # return HttpResponse("오늘 점심 뭐 먹지? 듣고 있나요? 듣고만 있나요? ")
    return render(request, 'main2.html')


def burger_list(request):
    burgers = Burger.objects.all()
    print(f"전체 햄버거 목록: {burgers}")
    return render(request, 'burger_list.html')