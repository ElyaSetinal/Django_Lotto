import random
from django.shortcuts import render

# Create your views here.
def extraction(request):
    #버튼 - 추출 명령 확인
    clickstate = request.GET.get('clickstate') #페이지 진입시 상태를 확인하여, 최초 진입시 출력되지 않도록 설정

    #랜덤 함수 이용 추출 시행
    #(나중에 할일) 6자리로 줄이고 보너스 번호를 별도로 출력하는 방식을 사용
    if clickstate == '로또 번호 추출하기': # html에서 들어오는 값이 submit 구문 value와 동일함
        lotto = sorted(random.sample(range(1,46), 7)) # ramdom 함수 사용 1~45번 중 7자리의 숫자 추출
        result = lotto # 결과(result)에 값 입력 - 출력부분 result를 lotto로 바꿈으로써 지울 수 있음
    else: #초기에 submit 입력이 되지 않았을때 출력되지 않도록 설정
        result = ' '

    #추출된 결과 출력
    return render(request, 'lottotemplate.html', {'result' : result})