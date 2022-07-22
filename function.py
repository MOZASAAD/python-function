#!/usr/bin/env python
# coding: utf-8

# # function : الدوال او الوظائف
# ## الداله او الوظيفه عباره عن مجموعه من العبارات
# ## statements 
# ## المرتبطه ببعضها والتي تؤدي مهمه محدده 

# # syntax : هيكل وشكل بناء الجمله 

# In[6]:


def function_name(parameters):
    
     """ docstring"""
    
     statement(s)
    
     reurn


# ##   def     
# ### : معناها تعريف وهي اختصار لكلمه         
# ## definition
# ## هي كلمه رئيسيه 
# ## Keyword
# ## تمثل بدايه راس الداله وتستخدم بتعريف الدوال والفئات .

# # name_function : اسم الداله 
# ### اسم الداله يجب ان ان يكون اسم فريد وتتبع تسميه الدوال نفس قواعد كتابه المعرفات في بايثون. 

# # parameters /arguments: المعاملات او الوسائط وهي العوامل التي تتغير في التجربه وهي متغيرات التي من خلالها نمرر القيم الى داله ، وهي قيم اختياريه 

# #   النقتطان (:): تستخدم لتحديد نهايه راس الداله  

# # docstring     
# ### :  سلسله التوثيق وهي اختصار لجمله 
# # documentation string 
# ### تستخدم هذه السلسه لوصف عمل الداله او الوظيفه .

# # statement : جمله او جمل بايثون وهي عباره عن جمله واحده او اكثر من جمله والتي تشكل جسم الداله ، 
# ### ويتم تنفيذها في كل مره يتم استدعاء الداله ويجب ان تحتوي هذه الجمل
# ### statements 
# ### على نفس مستوى المسافه البادئه 

# # return : ارجاع 
# ###   لتستخدم هذه الكلمه لإرجاع قيمه من الداله او للارجاع او للخروجمن الداله والعودة الى المكان الذي تم استدعائه منه
# 

# # كيفيه استدعاء الداله call a function 
# ### نقوم بكتابه اسم الداله مع معاملات التمرير 

# In[5]:


def greet(name):
 """
 This function greets to
 the person passed in as
 a parameter
 """
 print("Hello, " + name + ". Good morning!")
greet('mlaz')
greet('my dad')


# #  ويمكن استدعاء 
# # docstring
# # عن طريق كلمه 
# # __doc __

# In[6]:


print(greet.__doc__)


# # ACCESS POINT    
# ### : معامل الدخول ويرمز له بالرمز 
# ### ( . )
# ### هو معامل يستخدم للدخول داخا الداله 
# ### function
# ### او داخل الفئه 
# ### class
# ### وبالتالي يمكننا الحصول على خاصية او قيمه متغير من داخل الداله .

# # types of fubctions :انواع الدوال 
# ## built-in funcion : دوال مدمجه او مضمنه 
# ## user-defined function : دوال يحددها المستخدم 

# In[7]:


def add_numbers(x,y):
 sum = x + y
 return sum
num1 = 5
num2 = 6
print("The sum is", add_numbers(num1, num2))


# In[11]:


def greet(name, msg):
 """This function greets to
 the person with the provided message"""
 print("Hello", name + ', ' + msg)
greet("Mlaz", "yuo are good studant")
greet("my dad", "yuo are good father")
greet("my mam", "i miss you  ")
greet("my brother", "how are you")


# In[14]:


def greet(*names):
 """This function greets all
 the person in the names tuple."""
 # names is a tuple with arguments
 for name in names:
  print("Hello", name)
greet("mlaz", "my dad", "my mam", "mhmd")


# # function recursive : داله تكراريه 

# #  Recursion : معناها العوديه 
# # داله تستدعي نفسها 
# 

# In[2]:


def factorial(x):
 """This is a recursive function to find the factorial of an integer"""

 if x == 1:
  return 1
 else:
  return (x * factorial(x-1))
num =int(input("enter your number")) 
print("The factorial of", num, "is", factorial(num))


# # 1- تنتهي داله 
# # recursion
# # عندما ينتهي العدد الى 1 وهذا ما يسمى الشرط الاساسي
# # base condition

# # 2- يجب ان تحتوي كل داله تكراريه على شرط اساسي يوقف 
# # recursionٚ 
# # والا سوف يستدعي الداله نفسها بلا حدود 
# # infinitely

# # 3- يقلل 
# # interpreter
# # من التعمق واستخدام الداله 
# # recursionٌٍّ 
# # للمساعدة في تجنب العودة اللا نهائيه 
# # ِّinfinite recursions
# # مما يؤدي الى 
# # stack overflows

# # 4- بشكل افتراضي الحد الاقصى لعمق العوديه هو 1000 اذا تجاوزت الحد فانه ينتج عنه 
# # RecursionError

# # الداله المجهوله / لامدا 
# # (Anonymous / Lambda)

# In[6]:


double = lambda x: x * 2
print(double(9))


# In[14]:


x= int(input('ener  a number'))
double = lambda x: x * 2

print(double(x))


# In[ ]:


x= int(input('ener  a number'))
power = lambda x: x ** 2



print(power(x))


# # Anonymous : الداله المجهوله 
# ### هي داله يتم تعريفها بدون اسم ويتم تحديد الداله العاديه 
# ### باستخدام الكلمه الاساسيه 
# ### def 
# ### بينما يتم تحديد الداله المجهوله باستخدام الكلمه الاساسيه 
# ### lambda

# # Syntax

# ### يمكن ان تحتوي دوال
# ### Lambda
# ### على اي عدد من الوسيطات 
# ### argumentsٌٚ 
# ###  ولكن تحتوي على تعبير واحد فقط 
# ### expressionٚ

# In[ ]:


lambda arguments: expression


# ### تستخدم وظائف 
# ### lambdaِ
# ###  مع دوال 
# ### filterٚ()
# ### map()

# In[ ]:




