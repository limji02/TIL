## CSS Layout
  각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
  display(block, inline, flex, grid...)

## CSS Position
  요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
  다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등
  position(static, relative, absolute, fixed, sticky...)

  - 상, 하, 좌, 우 
  - 겹치는 요소의 쌓이는 순서 Z축 (수직방향)
  
- position 유형
  1. static
    nomal flow 기본 값
  2. relative
    상대 위치 (기준점 : 본인의 원래(static)위치)
    top, right, bottom, left 속성으로 위치 조정
    다른 요소의 레이아웃에 영향 X
    top: 100px;  ->  위에 공백을 주는 것이기 때문에 아래로 이동함
  3. absolute
    가장 가까운 relative 부모 요소를 기준으로 이동
    없을 경우 body를 기준으로 이동
    부모에게 relative를 주는 순간, 기준점을 잡을 수 있다.
    문서에서 요소가 차지하는 공간이 없어짐 (이것을 주의해야 함!)
    따라다니는 뱃지용으로 많이 쓴다.
  4. fixed
    문서에서 요소가 차지하는 공간이 없어짐
    화면 고정
  5. sticky
    relative(스크롤 위치가 임계점에 도달하기 전)와 fixed(스크롤 위치가 임계점에 도달 시)의 특성을 결합한 속성
    다음 sticky 요소가 나오면 이전 sticky 요소의자리를 대체

## Z-index
 요소의 쌓임 순서를 정의하는 속성

- 숫자가 큰 요소가 위에 쌓이게 된다.
- static이 아닌 요소에만 적용된다.
- 기본값은 auto, 부모 요소의 z-index 값에 영향을 받는다.
- 같은 부모 내에서만 값 비교, 값 같으면 HTML 문서 순서대로 쌓인다.
- 부모의 z-index가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없다!
- 무조건 맨 위에 있어야 하는 경우, 9999로 고정해둔다. 제한 없음.

    