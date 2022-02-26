#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests

urls = ['https://revistes.ub.edu/index.php/lectora/article/view/33302',
       'https://revistes.ub.edu/index.php/lectora/article/view/33044',
       'https://revistes.ub.edu/index.php/lectora/article/view/33063']
Title_List = []
Author_List = []
Keywords_List = []
Abstract_List = []
Issue_Number_List = []
for url in urls:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    Title = soup.find('h1', class_='page_title').text
    Title_List.append(Title)
    Author = soup.find('span', class_='name').text.replace(' ', '')
    Author_List.append(Author)
    Values = soup.find('section', class_='item keywords')
    Keywords = Values.find('span', class_='value').text.replace(' ', '')
    Keywords_List.append(Keywords)
    Abstract = soup.find('p').text
    Abstract_List.append(Abstract)
    Issue_Number = soup.find('a', class_='title').text.replace(' ', '')
    Issue_Number_List.append(Issue_Number)
df = pd.DataFrame(list(zip(Title_List,Author_List,Keyword_List,Abstract_List,Issue_Number_List)),columns=['Title','Author','Keywords','Abstract','Issue Number'])
df


# In[2]:


import pandas as pd
from bs4 import BeautifulSoup
import requests

urls = ['https://revistes.ub.edu/index.php/lectora/article/view/33302',
       'https://revistes.ub.edu/index.php/lectora/article/view/33044',
       'https://revistes.ub.edu/index.php/lectora/article/view/33063']
Title_List = []
Author_List = []
Keywords_List = []
Abstract_List = []
Issue_Number_List = []
for url in urls:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    Title = soup.find('h1', class_='page_title').text
    Title_List.append(Title)
    Author = soup.find('span', class_='name').text.replace(' ', '')
    Author_List.append(Author)
    Values = soup.find('section', class_='item keywords')
    Keywords = Values.find('span', class_='value').text.replace(' ', '')
    Keywords_List.append(Keywords)
    Abstract = soup.find('p').text
    Abstract_List.append(Abstract)
    Issue_Number = soup.find('a', class_='title').text.replace(' ', '')
    Issue_Number_List.append(Issue_Number)
df = pd.DataFrame(list(zip(Title_List,Author_List,Keyword_List,Abstract_List,Issue_Number_List)),columns=['Title','Author','Keywords','Abstract','Issue Number'])
df


# In[30]:


import pandas as pd
from bs4 import BeautifulSoup
import requests

urls = ['https://revistes.ub.edu/index.php/lectora/article/view/33277',
        'https://revistes.ub.edu/index.php/lectora/article/view/33302',
        'https://revistes.ub.edu/index.php/lectora/article/view/33044',
        'https://revistes.ub.edu/index.php/lectora/article/view/33063']
Title_List = []
Author_List = []
Keywords_List = []
Abstract_List = []
Issue_Number_List = []
for url in urls:
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, 'lxml')
    Title = soup.find('h1', class_='page_title')
    Title_List.append(Title.text.strip())
    Author = soup.find('span', class_='name')
    Author_List.append(Author.text.strip())
    Values = soup.find('section', class_='item keywords')
    Keywords = Values.find('span', class_='value')
    Keywords_List.append(Keywords.text.replace('\n','').replace('\t',''))
    Abstract = soup.find('p')
    Abstract_List.append(Abstract.text.strip())
    Issue_Number = soup.find('a', class_='title')
    Issue_Number_List.append(Issue_Number.text.strip())
df = pd.DataFrame(list(zip(Title_List,Author_List,Keywords_List,Abstract_List,Issue_Number_List)),columns=['Title','Author','Keywords','Abstract','Issue Number'])
df


# In[ ]:




