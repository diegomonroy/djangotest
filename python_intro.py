# Strings

>>> "Ola"
>>> "Hola " + "Ola"
>>> "Ola" * 3
>>> "Runnin' down the hill"
>>> 'Runnin\' down the hill'
>>> "Ola".upper()
>>> len("Ola")
>>> len(str(304023))

# Variables

>>> name = "Ola"
>>> name
>>> len(name)
>>> a = 4
>>> b = 6
>>> a * b

# Función print

>>> name = 'Maria'
>>> name
>>> print(name)

# Listas

>>> lottery = [3, 42, 12, 19, 30, 59]
>>> len(lottery)
>>> lottery.sort()
>>> print(lottery)
>>> lottery.reverse()
>>> print(lottery)
>>> lottery.append(199)
>>> print(lottery)
>>> print(lottery[0])

# Diccionarios

>>> participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
>>> print(participant['name'])
>>> participant['favorite_language'] = 'Python'
>>> participant.pop('favorite_numbers')

# Compara

>>> 5 > 2
>>> 3 < 1
>>> 5 > 2 * 2
>>> 1 == 1
>>> 5 != 2

>>> 6 >= 12 / 2
>>> 3 <= 2

>>> 6 > 2 and 2 < 3
>>> 3 > 2 and 2 < 1
>>> 3 > 2 or 2 < 1

# Boolean

>>> a = True
>>> a

>>> a = 2 > 5
>>> a

# Archivo

print('Hello, Django test!')

# If...elif...else

if 3 > 2:
	print('It works!')

if 5 > 2:
	print('5 is indeed greater than 2')
else:
	print('5 is not greater than 2')

name = 'Sonja'
if name == 'Ola':
	print('Hey Ola!')
elif name == 'Sonja':
	print('Hey Sonja!')
else:
	print('Hey anonymous!')

# Funciones

def hi():
	print('Hi there!')
	print('How are you?')
hi()

def hi(name):
	if name == 'Ola':
		print('Hi Ola!')
	elif name == 'Sonja':
		print('Hi Sonja!')
	else:
		print('Hi anonymous!')
hi("Ola")

def hi(name):
	print('Hi ' + name + '!')
hi("Rachel")

# Bucles

def hi(name):
	print('Hi ' + name + '!')
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
	hi(name)
	print('Next girl')

for i in range(1, 6):
    print(i)

# ORM de Django

# Ver todos los objetos

>>> from blog.models import Post
>>> Post.objects.all()

# Crear objetos

>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> me = User.objects.get(username='ola')
>>> Post.objects.create(author=me, title='Sample title', text='Test')

# Filtrar objetos

>>> Post.objects.filter(author=me)
>>> Post.objects.filter(title__contains='title')

>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())

>>> post = Post.objects.get(id=1)
>>> post.publish()
>>> Post.objects.filter(published_date__lte=timezone.now())

# Ordenando objetos

>>> Post.objects.order_by('created_date')
>>> Post.objects.order_by('-created_date')