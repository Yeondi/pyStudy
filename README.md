# pyStudy

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FYeondi%2FpyStud%25E3%2585%259B&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

부산대 python스터디 코드 공유 git

우측 위에 CODE 초록색 누르고 zip으로 다운받고 열면 끝!
py파일 그대로 올릴거라
vsCode에 드래그앤 드랍을 하던가
혹은
파일 우클릭 -> 연결프로그램 -> vsCode 혹은 메모장

열어서 코드 확인!
## <b>10818 2562 제외하고 나머지는 주석을 달아서 좀 더 이해가 되도록 해놨음!

  
& C:\pythonStudy C:\pythonStudy\sjh.py
^
 SyntaxError: invalid syntax
  
이런거 나오면 우측 하단 python쪽에 마우스 올려서 휴지통 눌러서 터미널 삭제하고 다시 실행!
  
# ===============================================================================
 format함수의 기본형은 "문자열 {변수}".format(값)이야.
 
 예로들어 date = 11
 str = "{}일 파이썬 스터디".format(date)
 print(str)
 출력 : 11일 파이썬 스터디
 이렇게 출력 돼
  {}를 그냥 쓰면 변수 있는 그대로 출력되고
  {0:0.3f} 이렇게 쓰면 format의 0번째 인덱스의 값을 float형으로 변환하고 소수점을 3자리로 강제하겠다라는 뜻이야.
  이렇게 쓰면 50.0이나와도 50.000 이렇게 쓰여
  
  print("{0:03d}번째의 진행도는 {1:0.3f}입니다.".format(nNum,fProcess))
  변수에 할당안하고 바로 print도 가능해
  이러면 0번째인 nNum은 3자리 정수로 강제하며, 1번째 fProcess는 float형의 소수점 셋째자리까지 표시한다. 라는뜻으로
  
  예) 005번째 진행도는 59.669입니다.
  이렇게 나와
  
  
