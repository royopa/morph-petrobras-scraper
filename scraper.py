# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import pandas as pd

# dados da petrobrás a partir de 2018-09-18
url = 'http://www.petrobras.com.br/lumis/api/rest/pricegraphnovo/pricedata?n=4'
df = pd.read_json(url)
df.columns = ['data_publicacao', 'data_variacao', 'vr_diesel', 'vr_gasolina']

for index, row in df.iterrows():
    print('Saving info from {}'.format(row['data_publicacao']))
    scraperwiki.sqlite.save(unique_keys=['data_publicacao'], data={
      'data_publicacao': row['data_publicacao'],
      'data_variacao': row['data_variacao'],
      'vr_diesel': row['vr_diesel'],
      'vr_gasolina': row['vr_gasolina']
    })
