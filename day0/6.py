md = {}
a = input().lower().replace(',', '').replace('.', '').split(' ')
for i in a:
    if i:
        if i in md:
            md[i] += 1
        else:
            md[i] = 1
for i in sorted(list(md.keys())):
    print(i, ': ', md[i])
