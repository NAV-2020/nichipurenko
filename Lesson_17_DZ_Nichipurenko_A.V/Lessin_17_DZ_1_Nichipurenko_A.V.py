'''
Задание 1
Пользователь вводит с клавиатуры строку. Проверьте
является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
слева направо и справа налево. Например, кок; А роза
упала на лапу Азора; доход; А буду я у дуба.
'''

def palindrome(messag_e: int) -> None:

   message_1 = messag_e.replace(" " , "").lower() 
   if message_1 == message_1[::-1]:
      print(messag_e, ' - palindrome\n')
      input('Press to continue...')
   else:
      print(messag_e, ' - not palindrome\n')
      input('Press to continue...')


if __name__ == "__main__":

   TEXT = 't'
   EXIT = 'q' 

   print('''
   Пользователь вводит с клавиатуры строку. Проверьте
   является ли введенная строка палиндромом. Палиндром — 
   слово или текст, которое читается одинаково слева направо 
   и справа налево. Например, кок; А роза упала на лапу Азора; 
   доход; А буду я у дуба.''')

   while True:

      print("""
      To exit press -> q
      Press to enter text -> t
      """)
      
      choice = input('Input: ')
      print()

      if choice == EXIT:
            break

      elif choice == TEXT:
         messag_e = input("Enter the string: ")
         print("-" * 50)
         palindrome(messag_e)