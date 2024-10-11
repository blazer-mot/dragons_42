input_data = open('input.txt', 'r',) # ВАЖНО!!!  не забыть создать файл; открытие файла ввода
data = input_data.read()
data = data.split()
N = int(data[0]) # преобразование строки в число
if N == 1:
    out = 1 
    output_data = open('output.txt', 'w') 
    output_data.write(str(out))
elif N == 2:
    out = 2
    output_data = open('output.txt', 'w') 
    output_data.write(str(out))
elif N % 3 == 0:
    a = N // 3
    out = 3**a
elif N % 3 == 1:
    a = (N - 2) // 3 
    out = 3**a * 2 * 2  
elif N % 3 == 2:
    a = N //3
    out = 3**a * 2
output_data = open('output.txt', 'w') # созпдние и открытие файла для вывода ответа
output_data.write(str(out)) # преобразование числа в строку при выводе и сам вывод
input_data.close() # закрытие файла считывания 
output_data.close() # закрытия файла вывода