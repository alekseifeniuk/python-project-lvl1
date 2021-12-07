import datetime
import functions

# Вводим имя и возраст
name = str(input('Enter name: '))
age = int(input('Enter age: '))

# Проверяем возраст на адекватность
age_is_right = functions.age_verification(age)

marital_status = str(input('Are You married? '))

# Узнаем текущие дату и время
real_date_time = datetime.datetime.today()

current_date = real_date_time.strftime('%d/%m/%Y')
current_time = real_date_time.strftime('%H-%M-%S')

# Записываем в файл данные о пользователе
f = open('/home/alexeyf/Desktop/USER_DB.txt', 'a')
f.write('User has joined {} in {}.'.format(current_date, current_time) + '\n')
f.write('Username: ' + name + '\n')
f.write('Password: ' + functions.password() + '\n')
f.write('Greeting: ' + functions.user_resume(name, age_is_right, marital_status) + '\n')
f.write('------------------------------------' + '\n')
f.close()
