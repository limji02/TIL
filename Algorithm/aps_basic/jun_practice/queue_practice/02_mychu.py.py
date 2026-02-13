# 큐의 활용 예시인 마이쮸 문제를 리스트의 pop(0)을 사용하여 구현해보기

def mychu_simulation(total_candy):
    # 큐에는 (학생 번호, 받을 개수) 튜플을 저장
    queue = [(1, 1)] 
    
    last_student = 0  # 마지막으로 마이쮸를 받은 학생 번호(답)가 될 것이다. 계속 얘를 갱신할 것
    next_student = 2  # 다음에 줄 설 학생 번호

    print(f"=== 마이쮸 {total_candy}개 나누기 시작 ===")

    while total_candy > 0:
        # [실습 1] 큐의 맨 앞에서 학생을 꺼내세요. (리스트 pop 활용)
        # 그 학생의 번호와 그 학생이 원하는 마이쮸의 개수
        student_id, want = queue.pop(0) # TODO
        
        # [실습 2] 줄 사탕 개수 결정 (남은 게 부족하면 남은 만큼 다 줘야하기 때문에...)
        give = min(want, total_candy)  # TODO (min 함수 활용 추천)
        # 준 만큼 빼기
        total_candy -= give
        # 마지막 학생 갱신
        last_student = student_id
        print(f"{student_id}번 학생이 {give}개 받음 (남은 개수: {total_candy})")

        # 사탕 다 떨어졌다... 남은 거 다 주면 종료
        if total_candy == 0:
            break

        # 그런데, 사탕이 다 안 떨어졌다?
        # [실습 3] 사탕을 받은 학생은 '받을 개수'를 1개 늘려서 다시 줄을 섭니다.
        # TODO: queue.append 사용
        queue.append((student_id, want + 1))
        
        # [실습 4] 새로운 학생이 줄을 섭니다. (항상 1개부터 시작)
        # TODO
        queue.append((next_student, 1))
        next_student += 1
        
    print(f"마지막 사탕의 주인공은 {last_student}번 학생입니다!")

# 실행
mychu_simulation(20)  # 마지막 사탕의 주인공은 2번 학생입니다!

# queue가 선입선출 형태로 움직이는 것을 보여주는 예시!!