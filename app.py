import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


headers= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

ticker = 'VALE'

urls = {}
urls['income annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/"
urls['income annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/"
urls['income quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/?period=quarterly"
urls['balance sheet annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/"
urls['balance sheet quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/?period=quarterly"
urls['cash flow annually'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/"
urls['cash flow quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/?period=quarterly"
urls['ratio annually'] = f"https://stockanalysis.com/stocks/aapl/financials/ratios/"
urls['ratio quarterly'] = f"https://stockanalysis.com/stocks/aapl/financials/ratios/?period=quarterly"

xlwriter = pd.ExcelWriter(f'financial statements ({ticker}).xlsx', engine='xlsxwriter')

for key in urls.keys():
    response = requests.get(urls[key], headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    #df = pd.read_html(StringIO(str(soup)), attrs={'data-test': 'fintable'})[0]
    df = pd.read_html(StringIO(str(soup)), attrs={'data-test': 'financials'})[0]
    df.to_excel(xlwriter, sheet_name=key, index=False)
xlwriter.close()