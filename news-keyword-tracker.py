#! python3

import bs4, requests, smtplib

#email address to send info to
email_address = 'example@email.com'

#keywords to search
keywords = ['keyword1', 'keyword2', 'keyword3']
any_present = False

#news sites to search
websites = ['https://www.cbc.ca/news', 'https://www.cbc.ca/news/canada', 'https://www.cbc.ca/news/canada/north']

#download and parse page
#should check each listed page for each listed keyword
for site in websites:
  get_news = requests.get(site)
  get_news.raise_for_status()
  news_page = bs4.BeautifulSoup(get_news.text, 'html.parser')
  news = news_page.select('.headline')
  for headline in news:
    for i in range(len(headline.text)):
      for keyword in keywords:
        segment = site.text[i:i+len(keyword)].lower()
        if segment == keyword:
          any_present = True
          
#send email if any keywords are present in any of the headlines on any of the pages
if any_present == True:
  con = smtplib.SMTP('smtp.gmail.com', 587)
  con.ehlo()
  con.starttls()
  con.login('example@email.com', 'app_key')
  con.sendmail('example@email.com', email_address, 'Subject: News Notification: %s is on %s', keyword, website)
  con.quit()
      

