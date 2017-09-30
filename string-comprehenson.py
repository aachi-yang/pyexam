

markers = [(97,64),(45,84), (1,2)]
result = ''.join("&markers=%s" % ','.join(map(str, x)) for x in markers)
print(result)

str = '01123456789'
result = ''.join((x) for n, x in enumerate(str) if n % 2 == 0)
print(result)

