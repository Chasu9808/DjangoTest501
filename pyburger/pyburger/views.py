from django.http import HttpResponse
from django.shortcuts import render

# views - controller 역할.
def main(request):
    # 단순 문자열만 리턴,
    # return HttpResponse("Hello, world.")
    # 화면을 연결해서 응답하기.
    return render(request, 'main.html')


def main2(request):
    # return HttpResponse("오늘 점심 뭐 먹지? 듣고 있나요? 듣고만 있나요? ")
    return render(request, 'main2.html')