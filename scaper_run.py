import glassdoor_scraper as gs
#import kenJee_glassdoor_scraperper as kgs
import pandas as pd
path ="D:/projects/ds_salary_proj/chromedriver_win32/chromedriver.exe"
print("Before Function")
df = gs.get_jobs('data scientist',15,False,path,15)
#df = kgs.get_jobs('data scientist',15,False,path,15)
#   print("After Function")