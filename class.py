#클래시 뒤의 이름은 무조건 대문자로 시작해야 한다.
class Animal:
    #필드 ,벰버변수
    type
    name
    age
    
    
class Animal1:
    #첫번째는 무조건 self 이고 self는 클래시 애니멀 나머지는 매개변수 
    def __init__(self,type,name,age):
        self.type=type
        self.name=name
        self.age=age

dog = Animal1('냉장고','뽀삐',5)
cat = Animal1('카페','야옹이',3)

print(dog.type,dog.name,dog.age)
print(cat.type,cat.name,cat.age)
#주민등록증 운전면허증 구별방법 다른타입

#자기소개(먼저할때 강아지이름은 뽀삐입니다 할거 적어놓고 나중에 하나씩 수정)
def introduce(self):
        print(f'self.type)의 이름은 (self.name)입니다')

dog.introduce()