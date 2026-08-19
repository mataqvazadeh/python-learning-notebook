# with open('text04.txt', mode='w', encoding='utf-8') as f:
#     f.write('My Writing sample')
#     print(f.tell())
#     f.write('Ha Ha HA\n')
#     print(f.tell())
#     f.write('\n\n\nMohammad\n')
#     print(f.tell())

with open('text_root.txt', mode='w+', encoding='utf-8') as file:
    lst = ['Hello\n', 'World\n', 'Ali']
    file.writelines(lst)
    file.seek(0)
    print(file.read())
