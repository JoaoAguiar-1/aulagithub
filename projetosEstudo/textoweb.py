import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.pudim.com.br')
#print(type(response))
#html = response.text
#print(html)
#print(response.status_code)
'''
100-199 Respostas informativas
200-299 Respostas bem-sucedidas
300-399 Mensagens de redirecionamento
400-499 Respostas de erro do cliente
500-599 Respostas de erro do servidor
'''

if (response.status_code >= 200) and (response.status_code <=299):
    print(response.text)

response = requests.get('http://github.com/', allow_redirects=False)
print(response.status_code)
