import requests
from bs4 import BeautifulSoup


def decodeSecretMessage(url):
  
  def tableDataText(table):    
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row       
    return rows


  # Making a GET request
  r = requests.get(url)

  # check status code for response received
  # success code - 200
  print(r)

  # Parsing the HTML
  soup = BeautifulSoup(r.content, 'html.parser')


  htmlTable = soup.find("table")
  table = tableDataText(htmlTable)

  # remove header:
  table = table[1:]

  # determine size of printedTable
  max_y = float("-inf")
  max_x = float("-inf")
  for row in table:
    max_x = max(max_x, int(row[0]))
    max_y = max(max_y, int(row[2]))

  printedTable = [[' ' for _ in range (max_x +1)] for _ in range(max_y +1)]

  for row in table:
    x, char, y = row
    x = int(x)
    y = int(y)
    printedTable[y][x] = char

          
  for row in (printedTable):
    print(''.join(row))

decodeSecretMessage('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')