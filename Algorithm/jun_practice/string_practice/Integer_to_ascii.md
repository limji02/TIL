## 연습문제_2_Integer_to_ascii

## 코드 설명

1. **0 예외 처리**
    
    ```python
    if integer_value == 0:
        return '0'
    ```
    
    - 만약 입력 값이 0이면, while 루프를 돌지 않고 빈 문자열이 반환되는 문제가 생길 수 있습니다.
    - 이를 사전에 방지하기 위해, 즉시 `'0'`을 반환하도록 합니다.
2. **음수 판별 및 양수화**
    
    ```python
    is_negative = (integer_value < 0)
    if is_negative:
        integer_value = -integer_value
    ```
    
    - 만약 음수라면, 양수로 바꿔서 문자열 생성 과정을 단순화합니다.
    - 나중에 결과 문자열에 `'-'`를 붙이면 음수 표시가 가능합니다.
3. **반복문을 통한 문자열 생성**
    
    ```python
    result_str = ''
    while integer_value > 0:
        remainder = integer_value % 10
        result_str = chr(48 + remainder) + result_str
        integer_value //= 10
    ```
    
    - 10으로 나눈 **나머지**(일의 자리)를 구해, `chr(48 + remainder)`로 숫자(0~9)에 해당하는 문자를 얻습니다.
        - 예: `remainder=5` → `chr(48+5) = chr(53) = '5'`
    - 새로운 문자를 기존 문자열 앞에 계속 붙여서(‘거꾸로’ 합치는 방식) 완성합니다.
    - 반복 시에는 10으로 나눈 **몫**을 다시 integer_value에 할당하여, 각 자리수를 처리해 나갑니다.
4. **음수 처리 후 결과**
    
    ```python
    if is_negative:
        result_str = '-' + result_str
    ```
    
    - 만약 처음에 음수였다면, 최종 문자열 앞에 `'-'`를 붙입니다.