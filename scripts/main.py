import os
import subprocess
from time import sleep

from scrap_news_channel import scrap_headlines
from text_to_speech import convert_headlines_to_speech
from parse_argments import get_new_channel

news_channel = get_new_channel()
print(f'Scraping {news_channel}')
headlines = scrap_headlines(news_channel)
print('Scripts executed succesfully.\nStarting to read the Headlines via default media player.')
convert_headlines_to_speech(headlines)
