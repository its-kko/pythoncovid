
from covid import Covid
import smtplib 
import os
import time

covid = Covid()
email = os.environ['email']
password = os.environ['password']
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(email,password)
work = True
server.sendmail(email,'mgkokooo2006@iclud.com',"HELLO")
while True:
    while work == True:
        mm = covid.get_status_by_country_id(28)
        c = mm['confirmed']
        d = mm['deaths']
        r = mm['recovered']
        time.sleep(300)
        mm2 = covid.get_status_by_country_id(28)
        c2 = mm2['confirmed']
        d2 = mm2['deaths']
        r2 = mm2['recovered']
        if c != c2:
            work = False

    while work == False:
        server.sendmail(email,'mgkokooo2006@icloud.com',
        f"""confirmed-{c2}
        deaths-{d2}
        recovered-{r2}
        New-Confirmed{c2-c}
        NewDeaths-{d2-d}
        NewRecoverd-{r2-r}
        """)
        work = True 