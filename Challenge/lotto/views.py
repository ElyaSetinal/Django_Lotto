import random
from django.shortcuts import render

# Create your views here.
#Input Page
def gcount(request): #게임수 입력 요청
    GCounter = request.GET.get("Gcount") #게임 수 받아오기
    return render(request, 'Lotto_Chall_In.html') #입력용 페이지 설정

#Output Page
def c_extract(request): #게임 수 및 로또번호 출력
    #게임 횟수 받기 및 공백 검증
    Gcount = request.GET.get('Gcount')
    if Gcount.isdigit() == True: # 숫자인지 판단
        Countcheck = int(Gcount)
    else: #int외의 입력이 들어오는 경우, 에러가 발생하므로 이를 방지하는 부분
        Countcheck = 0

    #연산 기능
    if Countcheck >0 : #게임 수가 0이상인 경우
        Gcounter = int(Gcount) # 반복문을 사용하기 위한 초기값
        lotto_List =[] # 번호 리스트를 담기위한 초기값
        while Gcounter > 0: #게임수가 0 초과 일때,
            lotto_C = sorted(random.sample(range(1,46), 7)) # ramdom 함수 사용 1~45번 중 7자리의 숫자 추출
            lotto_List.append(lotto_C) # 추출된 로또번호 리스트 하나의 리스트에 입력
            Gcounter -= 1 #게임 수 차감
        result = lotto_List # 결과 입력

    else:
        result = '정해진 게임 수가 없습니다.' #게임 수가 0이거나, 숫자가 아닐때 출력 값

    #응답
    return render(request, 'Lotto_Chall_Result.html', {'Game_count' : Countcheck, 'result':result})