import hashlib

i = 0
while True:
    p = (f'iwrupvqb{i}')
    text = p.encode()
    t = hashlib.md5(text).hexdigest()

    if t[:6] == '000000':
        print(i)
        break

    i += 1
