# -*- coding: utf-8 -*-
import pandas as pd
import scraperwiki


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
