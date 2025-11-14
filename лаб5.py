1.
#a = input().lower().strip()
#if a.isalnum():
#    print('Имя корректно')
#else:
#    print('Ошибка')
2.
#a = input()
#a = list(a)
#k = 0
#n = 0
#for i in range(len(a)):
#    if a[i].isdigit():
#        k += 1
#    elif a[i].upper()==a[i]:
#        n+= 1
#if len(a)>=8 and k>0 and n>0:
#    print('Пароль надёжен')
#else:
#    print('Пароль слаб')
3.
#log = 'ACCESS DENIED'
#print(log.capitalize()+' – вход запрещён')
4.
#data = "ERROR connection ERROR failed access"
#a = data.replace('ERROR',"ALERT")
#print(a,data.count('ERROR'))
5.
#a = input()
#if a[a.find('@')+1:].endswith('gmail.com'):
#    print(f'Домен: {a}')
#else:
#    print('Некорректный адрес')
6.
#a = input().strip().lower()
#a = a.replace(' ','_')
#print(a)
7.
#a = input()
#c = a.find('SECRET')
#for i in range(c,c+6):
#    a = a.replace(a[i],'*')
#print(a)
8.
#s =''
#a = input()
#for i in range(len(a)):
#    print(a[i],'-',ord(a[i]))
#    s = s + chr(ord(a[i]))
#print(s)
9.
#text = "login attempt failed access denied unauthorized access"
#if text.count('failed') + text.count('denied')>0:
#    print("Попытка несанкционированного доступа")
#    print(f'{text.count('denied')}-denied   {text.count('failed')}-failde ')
10.
#a = input().lower()
#print(f'{a.count('.')}-точки {len(a)-a.count(' ')}-кроме пробелов')
#print(f'{a.startswith('report')}-начинается ли с Report')
#if a.count('error')>=2:
#    print("Ошибки найдены")


#1. Строка в Python — это неизменяемая последовательность символов в кавычках
#2. Unicode — универсальный стандарт кодирования символов, используемый для поддержки всех языков и символов
#3. strip(), replace(), find() — удаляет пробелы по краям, заменяет подстроку, ищет подстроку и возвращает её индекс.
#4. Количество вхождений подстроки** считается с помощью count().
#5. upper() делает всю строку заглавной, capitalize() только первый символ.
#6. ord() возвращает код символа, chr() — символ по коду.
#7. Проверить начало строки можно методом startswith().
#8. Фильтрация данных важна, чтобы предотвратить ошибки и некорректные действия программы.