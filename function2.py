x=1
def func(a):
  return a+x

print(func(1))

def func2(a):
  x = 2
  return a+x

print(func2(2))

def times( a = 10, b = 20):
  return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURL(server, port):
  serverURL = "http://"+server+":"+port
  return serverURL

print(connectURL("dredu.com", "80"))
print(connectURL( port="80", server = "dredu.com"))



def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))