
## CSS Box Model - display 속성
박스의 화면 배치

- 박스 타입
  1. Block
    항상 새로운 행으로 나뉨(한 줄 전체 차지) *Normal flow
    width, height, margin, padding 가능
    다른 요소를 밀어내기 가능
    width 속성 미지정시, inline 방향(좌우) 사용 가능한 공간 모두 차이(너비 100%)
    h1~6, p, div, ul, li...

    - 대표 : div로 구조화  
  
  2. Inline
    줄을 바꾸지 않고, 텍스트 일부에만 다른 스타일 적용시 사용 *Normal flow
    width, height 사용 불가능
    padding, margin, border 적용, but 상하로는 다른 요소 밀어낼 수 없음
    a, img, span, strong, b, em...

    - 대표 : span 
  3. inline-block
    위의 두 가지 특징을 섞어 가진 특별한 display 속성 값
    줄 바꿈 없이, 크기 지정 가능!
    padding, margin, border로 방향 상관없이 밀어내기 가능

  4. none
    요소를 화면에 표시하지 않고, 공간도 부여 안 됨
    후보 선수
    사용자와 상호 작용시 쓰이게 될 예정, JS

  5. flex

