import requests
from bs4 import BeautifulSoup

url = "https://www.tamilnaducareers.in/tn-govt-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table',class_='tc_table_pages')
column1_data = []
column2_data = []
column3_data = []
column4_data = []
column5_data = []
s=[]
x=table.find_all('tr')
# Iterate through table rows
for row in x:
    # Find all cells in the row
    cells = row.find_all('td')
    # Assuming the first cell corresponds to the first column, and so on
    if len(cells) >= 2:  # Assuming there are at least 2 cells per row
        column1_data.append(cells[0].text.strip())
        column2_data.append(cells[1].text.strip())
        column3_data.append(cells[2].text.strip())
        column4_data.append(cells[3].text.strip())
        column5_data.append(cells[4].text.strip())
for x in column4_data:
    c=str(x).split(',')
    for i in c:
        s.append(i)
set_=set(s) 
def qual():
    print('Enter your Qualification.. ')
    qu=input()
    print(' ')
    for x in range (len(column4_data)):
        if qu.casefold() in  str(column4_data[x]).casefold():
            print("Organization   :", column1_data[x])
            print("Post Names     :", column2_data[x])
            print("No of Vacancies:", column3_data[x])
            print("Qualification  :", column4_data[x])
            print("Last Date      :", column5_data[x])
            print('Apply Link     :',url)
            print('  ')
        else:
            pass
    else:
        print('There are the jobs for your Qualification '.title())
        print(' ')
        if input('If you want to continue? Y/N  : ').casefold()=='Y'.casefold():
            print('Hello ',name) 
            qual()
        else:
            print('Thank You ',name)  
print('Hi..sir/mam')
name=input("What's your Name sir/mam ?   ")
print(" ")
print('Hello ',name.capitalize())
print(" ")
print('I am Bot\nused for Finding Government jobs.. ')
print(" ")
for i in set_: 
    print(i.expandtabs(30),sep='|',end='|')
print(" ")
print(" ")
qual()
 