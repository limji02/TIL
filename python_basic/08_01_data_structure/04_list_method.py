################ 리스트 값 추가 및 삭제 ################

# append와 pop 중요!

# append
# append(x) - 리스트 마지막에 항목 x를 추가

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
# append는 None을 반환합니다.
# 반환 값이 없다. 무언가를 반환하는 게 아니라 원본에 추가한다. 
print(my_list.append(4))  # None

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# extend와 append의 비교
my_list.append([5, 6, 7])
print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]

# my_list.extend(100)  # TypeError: 'int' object is not iterable

# insert
# insert(i, x) x를 지정한 인덱스 i위치에 삽입
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]

# remove
# 리스트에서 첫 번째로 일치하는 항목을 삭제
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]
# 일치하지 않은 경우에는?

# pop
# pop() 또는 pop(i) 
# 리스트에서 지정한 인덱스의 항목을 제거하고 반환, 작성하지 않을 경우 마지막 항목을 제거 
# 알고리즘의 자료 구조를 표현할 때 append()와 함께 많이 쓰인다.
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]

# clear
# 빈 리스트로 만든다.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []


################ 리스트 정렬 및 순서 변경 ################

# reverse
# 정렬은 아니다. 리스트의 순서를 역순으로 변경하는 것이다.
# 반환 값이 없다. 원본을 뒤집을 뿐이다.
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# reverse는 None을 반환합니다.
# print(my_list.reverse())  # None
# reverse는 원본 리스트를 변경합니다.
print(my_list)  # [9, 1, 8, 2, 3, 1]

# sort
# 원본 리스트를 오름차순으로 정렬한다. 내림차순도 가능하다.
# sort는 리스트의 메서드이고, sorted는 내장 함수이며 인자를 다양하게 받을 수 있다.
# sort는 반환 값이 없고, sorted는 반환을 해준다.
my_list = [3, 2, 100, 1]
my_list.sort()
# sort는 None을 반환합니다.
# print(my_list.sort())  # None
# sort는 원본 리스트를 변경합니다.
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]


