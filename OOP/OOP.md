# Class
---
Cú pháp của class:<br>
```text 
class nameOfTheClass(parent_class):
    statement1
    statement2
    statement3
```
## Thuộc tính
###  Phạm vi truy cập thuộc 
- __Public__ là trạng thái công khai nhất trong ba mức độ, khi một thành phần trong class được khai báo ở dạng public tức là chúng ta có thể sử dụng được thành phần đó từ bất kỳ đâu trong chương trình. Và để khai báo một thành phần trong class là public thì mọi người chỉ cần tuân thủ quy tắc sau:

>> Tên của thành phần không được bắt đầu bằng ký tự _ mà phải bắt đầu bằng chữ cái.

- __Protected__ nằm ở mức độ thứ 2. Khi một thành phần trong class được khai báo là protected thì nó chỉ có phạm vi sử dụng ở trong class khởi tạo nó và class kế thừa từ class đó (class con) mà chúng ta sẽ không thể gọi được khi đứng từ bên ngoài class.
Nhưng, bản chất trong Python không tồn tại loại phạm vi này, do đó chúng ta quy chuẩn nó về protected mà bản chất của nó vẫn là public.
Để khai báo một thành phần là protected thì mọi người cần tuân theo quy tắc sau:
>> Tên của thành phần phải được bắt đầu bằng 1 ký tự _.

- __Private__ là phạm vị hẹp nhất trong lập trình hướng đối tượng, khi một thành phần trong đối tượng được khai báo ở dạng private, thì nó chỉ có phạm vi hoạt động ở trong class khai báo nó mà thôi.
Để khai báo một thành phần ở dạng private thì mọi người chỉ việc tuân thủ theo quy tắc sau:
>> Tên cả thành phần phải được bắt đầu bằng 2 ký tự __.
###
---
Thuộc tính là biến nằm trong một lớp. Thuộc tính mô tả các đặc tính của một đối tượng. Trong Python có một phương thức đặc biệt gọi là  __init __() dùng để khởi tạo giá trị cho các thuộc tính của một đối tượng.
```text 
class Cat:
    def __init__(self, name):
        self.name = name
```
Trong đoạn code trên, ta định nghĩa lớp Cat. Bên trong lớp này, ta định nghĩa phương thức __init __(). Phương thức __init __() là phương thức khởi tạo của tất cả các lớp, mỗi khi tạo một đối tượng phương thức này sẽ tự động được gọi.

>>def __init __(self, name):

Bất cứ phương thức nào của Python cũng đều phải có tham số đầu tiên là __self__ rồi mới đến các tham số khác. __self__ thực ra chỉ là biến đối tượng đã gọi phương thức này mà thôi.
>> self.name = name

Ở dòng trên ta khởi tạo thuộc tính name và gán giá trị cho nó.

>>missy = Cat('Missy')<br>
lucky = Cat('Lucky')

Trong hai dòng trên ta dùng hàm Cat() để tạo ra hai đối tượng lớp thuộc lớp Cat. ta _không trực tiếp_ đưa tham số self vào mà chỉ đưa các tham số thứ 2 trở đi thôi, self được tự động đưa vào bởi trình thông dịch.

__Note:__ Ngoài ra bạn có thể gán giá trị cho các thuộc tính ở bất cứ đâu sau phần định nghĩa lớp chứ không chỉ riêng bên trong phương thức khởi tạo.

```text 
class Cat:
    def __init__(self, name):
        self.name = name

boss = Cat("Boss")
boss.say = "meo meo meo"

print (boss.say)       
```

Một đặc điểm nữa trong Python, có thể định nghĩa các thuộc tính chung cho mọi đối tượng.
```text 
class Cat:
    species = 'mammal'
    def __init__(self, name):
        self.name = name


```

## Phương thức - method 
Phương thức chẳng qua là các hàm, chỉ khác hàm bình thường ở chỗ chúng được định nghĩa bên trong một lớp. Các phương thức được sử dụng để thực hiện các công việc cụ thể.

```text
class Circle:
    pi = 3.141592
 
    def __init__(self, radius=1):
        self.radius = radius 
 
    def area(self):
        return self.radius * self.radius * Circle.pi
 
    def setRadius(self, radius):
        self.radius = radius
 
    def getRadius(self):
        return self.radius
```
Phương thức __area()__ trả về diện tích hình tròn.
### set - get methods
##### Phương thức __set__ để cài đặt giá trị cho thuộc tinh 
```text 
def setRadius(self, radius):
    self.radius = radius
```
Phương thức setRadius() thiết lập giá trị cho thuộc tính radius (bán kính).

##### Phương thức __get__ để cài lấy giá trị thuộc tính
```text
def getRadius(self):
   return self.radius
```
Phương thức getRadius() trả về lấy giá trị bán kính.

## Kế thừa - inheritance
Kế thừa trong lập trình hướng đối tượng cho phép ta sử dụng lại mã nguồn và giảm độ phức tạp của chương trình. Lớp dẫn xuất có thể kế thừa hoặc mở rộng các tính năng của lớp cơ sở.
Cú pháp: <br>`
```text
class ChildClass(ParentClass1[, ParentClass2, ...]):
   statement_1
   .
   .
   statement_n
```
Ví dụ:<br>
```text 
class Animal:
   def __init__(self):
      print ("Animal created")
 
   def whoAmI(self):
      print ("Animal")
 
   def eat(self):
      print ("Eating")
 
 
class Dog(Animal):
   def __init__(self):
      Animal.__init__(self)
      print ("Dog created")
 
   def whoAmI(self):
      print ("Dog")
 
   def bark(self):
      print ("Woof!")
```
Trong ví dụ trên ta định nghĩa hai lớp là là _Animal_ và lớp _Dog_. Lớp Dog kế thừa từ lớp Animal, thừa hưởng một số phương thức của lớp Animal và có các phương thức của riêng nó. Ở trên lớp Dog kế thừa phương thức eat(), kế thừa và thay đổi phương thức whoAmI(), ngoài ra lớp Dog còn có phương thức của riêng nó là phương thức bark().


```text 
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ("Dog created")
```
Để kế thừa một lớp thì ta đặt tên lớp đó bên trong cặp dấu ngoặc tròn () ngay phía sau phần định nghĩa tên lớp. Nếu bên trong lớp cơ sở đã định nghĩa phương thức __init __(), ta phải gọi lại phương thức __init __() từ lớp cơ sở.
 
## Đa hình - Polymorphism

```text
class Animal:
   def __init__(self, name=''):
      self.name = name
 
   def talk(self):
      pass
 
 
class Cat(Animal):
   def talk(self):
      print ("Meow!")
 
 
class Dog(Animal):
   def talk(self):
      print ("Woof!")
```
Trong ví dụ trên, ta định nghĩa hai lớp chó (Dog) và mèo (Cat) kế thừa từ lớp Animal. Do đó cả hai lớp này đều kế thừa phương thức talk() của lớp Animal, nhưng mỗi lớp lại in ra hai dòng text khác nhau.
```text
c = Cat("Missy")
c.talk()
 
d = Dog("Rocky")
d.talk()

# Output:
Meow!
Woof!
```
---
---

# Khai báo abstract class
