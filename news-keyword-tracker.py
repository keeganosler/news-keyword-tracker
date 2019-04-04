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


