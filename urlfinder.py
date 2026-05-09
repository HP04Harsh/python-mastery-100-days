url = "ftp://www.google.com/chats"

protocol = url[:url.find(':')]
domain = url[url.find('.')+1:url.rfind('.')]
paths = url[url.find('/', url.rfind('.')):]

print(protocol, domain, paths)