first_str = 'i love my mom so much'
second_str = 'i love my dad so much'
thirg_str = 'i love my sister so much'
fourth_str = 'i love my dog so much'
file=open('text_file.txt', 'w')
file.write ('i love my mom so much\ni love my dad so much\n')
file.close
file=open('text_file.txt', 'a')
file.write ('i love my sister so much\ni love my dog so much\n')
file.close