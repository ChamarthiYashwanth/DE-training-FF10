# 2. Flow control
# control flow functions
# for loop
# while loop

# decision making
# if
# elif
# else

# encryption
a = list(map(lambda x: chr(x),range(97,123)))
d = {}
for i in a:
    d[i] = ord(i)+20
s = input()
i = 0
res = ''
while i < len(s):
    x = s[i]
    if x == ' ':
        res += ' '
    else:
        res += str(d[x])+' '
    i += 1
print('encrypted:',res)

# decryption
d_s = res
d_s = d_s.split()
de_res = ''
for i in d_s:
    if i == '':
        pass
    de_res += (chr(int(i)-20))
print('decrypted:',de_res)

# do while
pin = True
count = 0
while pin:
    print('done')
    count += 1
    if count == 1:
        break