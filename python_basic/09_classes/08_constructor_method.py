class Person:
    def __init__(self, name):
        self.name = name  # name 간의 연관성은 없다. 왼쪽 name은 인스턴스 변수명이고, 오른쪽 name은 매개변수이다. 다르게 해도 상관은 없으나, 추후 유지보수 시 편리성을 위해 똑같이 한다.

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.
# Person.greeting(person1) 실제 내부에서 동작하는 코드 - 해당 코드 또한 똑같이 동작하지만, 위의 코드가 자연스럽다.
print(person1.name)  # 지민