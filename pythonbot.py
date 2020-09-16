from covid import Covid
import smtplib 
import time
from threading import Timer
import os 
covid = Covid()
email = os.environ['email']
password = os.environ['password']
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(email,password)
server.sendmail(email,'mgkokooo2006@icloud.com',"Try")

def getdata():
    global mm,c,d,r
    mm = covid.get_status_by_country_id(28)
    c = mm['confirmed']
    d = mm['deaths']
    r = mm['recovered']
    time.sleep(5)
    global mm2,c2,d2,r2
    mm2 = covid.get_status_by_country_id(28)
    c2 = mm['confirmed']
    d2 = mm['deaths']
    r2 = mm['recovered']

def run():
    getdata()
    if c2 > c:
        server.sendmail(email,'mgkokooo2006@icloud.com',
        f"""confirmed-{c2}
        deaths-{d2}
        recovered-{r2}
        New-Confirmed{c2-c}
        NewDeaths-{d2-d}
        NewRecoverd-{r2-r}
        """)
        Timer(60,run).start()

run()