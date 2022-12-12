# string="over the lazy dog"
# string.split()
# from re import sub

# def camel_case(s):
#   s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
#   return ''.join([s[0].lower(), s[1:]])
# print(camel_case('JavaScript'))
# print(camel_case('Foo-Bar'))
# def camelCase(st):
#     output = ''.join(x for x in st.title() if x.isalnum())
#     return output[0].lower() + output[1:]

# def camelCase(st):
#     s = st.title()
#     d = "".join(s.split())
#     d = d.replace(d[0],d[0].lower())
#     return d
string="Lower case of the look"
s=string.lower()
text=s.split()
vlu=""
for i in range(len(text)):
  if i==0:
    vlu+=text[i]
  else:
    vlu+=text[i].capitalize()
print(vlu)
# str=string.split()
# i=0
# while str[i]==" ":
#   if str[i]=="":
#     str[i]=str[i].upper()
# print(str[i])

# T=int(input())
# for i in range(T):
#     N=int(input())
#     for j in range(N):
#         A=list(map(int,input().split()))
#         B=list(map(int,input().split()))
#         # a=set(A[j]+B[j])
#         a=(A[0]+B[0],A[1]+B[1],A[2]+B[2])
#         print(a)
#         print(max(a))