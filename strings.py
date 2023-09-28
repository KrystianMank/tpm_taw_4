'''
Strings
'''
a='jakieś zdanie'
b="maciej wojtal"
c='''
tekst
'''

# print(a[1:3])
# print(a[::-1])

# t1='alicja'
# t2='KOWALSKA'
# t3='2'
# print(t1+' '+t2)
# print(f"{t1} {t2}")
# print(f"Długość tekstu: {len(t1)}")

# print(t1.capitalize())
# print(t3.isdigit())
# print(t2.join(t1))

# x='a'
# t=''.join(x)
# print(t)

t='    Jan    Kowalski'
# print(t.replace('a','A'))

li='    Jan    Kowalski  Chojncie  '
li=li.split()

nowy=''
for t in range(len(li)):
    nowy+=li[t]
    if(t<len(li)-1):
        nowy+=' '

print(nowy)