# 백준 2941_크로아티아 알파벳
# implementation

c_alphabet = ['c=','c-', 'dz=', 'd-','nj', 'lj', 's=', 'z='] # 'dz=' 가 'z='보다 앞에 있어야함
#c_alphabet = ['c=','c-', 'z=', 'dz=', 'd-','nj', 'lj', 's='] # 이렇게 하면 'z='를 우선으로 바꿔서 오답
word = input()

for i in c_alphabet:
    if i in word:
        word = word.replace(i, "*")

print(len(word))