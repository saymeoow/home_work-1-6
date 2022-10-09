# Ввести предложение, состоящее из двух слов. Поменять местами слова, добавить "!" в начало и конец, слова разделить 3 символами (" ", "!", " ")
words = 'hello all'
splited_words = words.split()
first_word = splited_words[0]
second_word = splited_words[1]
task='!' + second_word + ' ' + '!' + ' ' + first_word + '!'
print(task)




words = ['hello','all']
words.reverse()
words.insert(0,'!')
words.insert(2,' ')
words.insert(3,'!')
words.insert(4,' ')
words.insert(6,'!')
print("".join(words))