# xkcdToMail
 sends today's xkcd webcomic through e-mail

webscrape xkcd.com, get the current comic on the release day of the week (monday, wednesday or friday) and sends the image through e-mail. If current day is not release day, sends a random comic.

modules used

    requests
    
    beautifulsoup4
    
    smtplib
    
    python-dotenv
    
    time
    
dotenv is used to secure credentials. To make the code work, a '.env' (db.env) file in the same directory as main.py must exist. Inside, change the represented value of the variables found in the code (password, email, emailto) as follows:

    PASSWORD = 'GmailPassword'
 
    EMAIL = 'GmailAddress'
 
    EMAILTO = recipientEmail1, recipientEmail2, recipientEmailn
 
You would be logging in directly to, in this case, gmail smtp server. No one would have access to it. Just make sure the db.env is included in the .gitignore.

There is also a fix pertaining dotenv working with raspbian crontab, if raspberrypi is used to run the script.
