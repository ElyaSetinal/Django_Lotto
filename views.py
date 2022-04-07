import random
from django.shortcuts import render

# Create your views here.
#Basic Mission

def extraction():
    #버튼 - 추출 명령 확인
    #버튼의 입력을 받는 코드가 필요

    #랜덤 함수 이용 추출 시행
    lotto = sorted(random.sample(range(1,46), 7)) # 1~45번 중 7자리의 숫자 추출
    result = lotto # 결과(result)에 값 입력 
    return result

    #최초에 안보이게 하고 싶은데 <22.04.03 해결, html에 clickstate를 추가>
    #새로고침으로도 안바뀌게 하고 싶은데
global cnt
cnt = 0
def checks(request): 
    global cnt
    print(f'cnt = {cnt}')
    if cnt == 2:
        cnt = 0
    if cnt%2 == 1:
        cnt += 1
        print(f'cnt2 = {cnt}')
        result = extraction()
        print(f'result = {result}')
        return render(request, 'lottotemplate.html', {'result' : result})
    else:
        cnt += 1
        print(f'cnt3 = {cnt}')
        return render(request, 'lottotemplate.html')