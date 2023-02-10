import requests, bs4, smtplib, os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#create a database to store environmental variables to secure smtp login credentials in the code
load_dotenv('db.env')
password = os.environ['PASSWORD']; email = os.environ['EMAIL']; email2 = os.environ['EMAIL2']

def xkcdScrap(url):

    #downloads the site into memory
    res = requests.get(url)

    #checks for download errors
    if not res.status_code == requests.codes.ok:
        print("Download failed\n")
        input()
        exit()

    #uses beautifulsoup to read all the html data (content) from the site
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    #gets the webcomic current no.
    numsource = bs4.BeautifulSoup(res.text, 'html.parser').select('html body div#middleContainer.box a')[1]['href'].strip()

    #from the html data, locate the image tag, css path, from the comic and selects it's first element [0], wich is the image it self
    img_tag = soup.select('html body div#middleContainer.box div#comic img')[0]

    #from the list of elements inside the tag, locate the url source of the image
    img_url = img_tag['src']
    img_url_full = 'https:' + img_url

    #saves the image's byte data into memory
    img_data = requests.get(img_url_full).content

    return img_data, numsource

def xkcdSend(img, num):

    #sets up MIMEemail to correctly send the image as an attached png conteiner
    #creates a conection obj with google's smtp as target
    #connects to server
    #sets up encrypted protocol
    #login
    #sends the e-mail, the image, to the recipient
   
    msg = MIMEMultipart()
    msg['Subject'] = 'XKCD webcomic no. ' + num
    
    text = MIMEText(' ')
    msg.attach(text)

    image = MIMEImage(img)
    msg.attach(image)

    with smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.ehlo()
        conn.starttls()
        conn.login(email, password)
        conn.sendmail(email, email2, msg.as_string())

    print('Sent!')

#runs the routines
img_data, numsource = xkcdScrap('https://xkcd.com')
xkcdSend(img_data, numsource)





