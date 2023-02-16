# xkcdToMail
 sends today's xkcd webcomic through e-mail

webscrape xkcd.com, get the current comic on the release day of the week (monday, wednesday or friday) and sends the image through e-mail. If current day is not release day, sends a random comic.

modules used

    requests
    
    beautifulsoup4
    
    smtplib
    
    python-dotenv
    
    time
    
dotenv is used to secure credentials. To make the code work, you'd need to create a db.env in the repo. and write in the values of the placeholders found in the code (email, email2 and password) as follows:

    PASSWORD = 'GmailPassword'
 
    EMAIL = 'GmailAddress'
 
    EMAIL2 = 'recipientEmail'
 
You would be logging in directly to, in this case, gmail smtp server. No one would have access to it. Just make sure the db.env is included in the .gitignore.

There is also a fix pertaining dotenv working with raspbian crontab, if raspberrypi is used to run the script.
