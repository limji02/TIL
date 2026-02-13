# 선형 큐를 구현해보고, 배열 앞쪽 공간이 비어있음에도 꽉 찼다고 인식하는 문제를 직접 눈으로 확인해보기
# 실전 문제에서는 리스트를 쓰면서 큐 활용. 아래와 같이 쓰지는 않는다.

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity  # 1. 공백 큐 생성 createQueue
        self.front = -1  # 머리 위치 초기화
        self.rear = -1  # 꼬리 위치 초기화

    def is_empty(self):
        # [실습 1] 큐가 비어있는 조건은? front = rear
        return self.front == self.rear  # TODO

    def is_full(self):
        # [실습 2] 선형 큐에서 꽉 찼다고 판단하는 조건은? (rear 위치 기준)rear가 끝에 가면 꽉 찼다고 판단한다!
        # rear가 큐의 최대 인덱스에 도달하면 꽉 찼다고 판단 (그러나... 선형 큐의 한계)
        return self.rear == self.capacity -1 # TODO

    def enqueue(self, item):
        if self.is_full():  # 만들었던 걸로 꽉 찼는지 일단 확인 후,
            print("Queue is Full!")
            return None
        # [실습 3] rear를 이동시키고 데이터를 저장하세요.
        # TODO
        self.rear += 1  # rear 인덱스를 1 증가
        self.items[self.rear] = item  # 새 항목을 rear 위치에 추가

        print(
            f"Enqueue({item}) -> {self.items} | front:{self.front}, rear:{self.rear}"
        )

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        # [실습 4] front를 이동시키고 데이터를 반환하세요.
        # TODO
        self.front += 1  # frint 인덱스를 1 증가
        deleted_item = self.items[self.front]  # front 위치의 항목을 가져옴
        self.items[self.front] = None  # 선택된 자리를 비우기 (굳이 안 바꿔도 되긴하는데 명확하게 보이려고 함)
        print(f"Dequeue() -> {item} | {self.items} | front:{self.front}, rear:{self.rear}")
        return deleted_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items[self.front + 1]  # front 다음 위치의 항목 반환

    def get_size(self):
        return self.rear - self.front  # 현재 큐에 있는 항목의 개수 계산


# --- 테스트 ---
print("=== 선형 큐 테스트 (크기 4) ===")
q = LinearQueue(4)

# 1. 큐 꽉 채우기
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(f"큐의 현재 크기: {q.get_size()}")
print(f"큐의 맨 앞 데이터 확인(peek): {q.peek()}")
print(f"큐 내부 리스트 상태: {q.items}\n")

2. 데이터 2개 꺼내기 (앞쪽 2칸이 비게 됨)
q.dequeue()
q.dequeue()
# dequeue를 두 번하면 front가...어떻게 될까요??

print(f"큐의 현재 크기: {q.get_size()}")
print(f"큐의 맨 앞 데이터 확인(peek): {q.peek()}")
print(f"큐 내부 리스트 상태: {q.items}")

# 3. [문제 상황] 빈 공간이 있는데도 추가 불가 (False Full)
print("\n--- False Full 발생 확인 ---")
q.enqueue(50)
# 자리는 비어 있는데 왜 q가 꽉차있다고 할까??
# enqueue 함수 실행 -> is_full 실행 - > rear가 큐의 최대 인덱스에 도달하면 꽉찬 것으로 간주함
# (앞에 두 개가 지워졌음에도 불구하고 꽉찼다고 출력한다는 ... 선형 큐의 한계점!)
# 이걸 어떻게 해결? 마치 원처럼 이동하는 것으로(생각만) 포인터의 위치를 재정비하면 된다. 원형 큐
# 인덱스가 순환하도록 하는 것이다.
# 원형 큐는 front와 rear의 인덱스를 순환시키겠다.
#
