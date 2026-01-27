############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # user_data에서 키를 하나씩 꺼낸다.
    for user in user_data:
        # 만약 그 키의 값이 빈 문자열 이라면?
        if user_data[user] == '':
            # 빈 문자열을 보자마자 결과를 내보내고 끝낸다.
            return False
        # else:
        #     return True # !! 첫 번째 항목이 비어있지 않으면 즉시 True를 반환하고 끝나므로 조건과 다르다.

    return True # 반복문이 완전히 끝날 때 까지 False가 안 나왔다면, 모든 값이 있는 것이다.



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################