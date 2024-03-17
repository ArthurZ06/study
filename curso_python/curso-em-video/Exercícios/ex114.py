import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site Pudim não da pra acessar agora :(\033[m')
else:
    print('\033[36mDeu tudo certo você conseguiu entrar no site :)\033[m')
