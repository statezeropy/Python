import os
import smtplib
from email import encoders
from email.utils import formataddr
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from_addr = formataddr(('Youhost', 'kimjy@youhost.co.kr'))
to_addr = formataddr(('TEST', 'nashirah23@naver.com'))


s = smtplib.SMTP('mail.youhost.co.kr', 587)
s.ehlo()
s.starttls()
#s.login('kimjy@youhost.co.kr', 'passwd')

msg = MIMEMultipart('mixed')
msg.set_charset('utf-8')
msg['Subject'] = 'Test1'
msg['From'] = from_addr
msg['To'] = to_addr
body = '''
안녕하세요.
클라우드기술팀 김주영입니다.

빅테이터 CPU 주간 사용량 작성을 위한 첨부파일 전달용 메일입니다.
'''
bodyPart = MIMEText(body, 'html', 'utf-8')
msg.attach(bodyPart)

attachments = list()
attachments.append('C:/Users/KJY/Downloads/bigdataCPU_0913_kimjy_20220913171124.pdf')


for attachment in attachments:
    attach_binary = MIMEBase("application", "octect-stream")
    try:
        binary = open(attachment, "rb").read() # read file to bytes

        attach_binary.set_payload( binary )
        encoders.encode_base64( attach_binary ) # Content-Transfer-Encoding: base64
        
        filename = os.path.basename( attachment )
        attach_binary.add_header("Content-Disposition", 'attachment', filename=('utf-8', '', filename))
        
        msg.attach( attach_binary )
    except Exception as e:
        print( e )



s.sendmail(from_addr, to_addr, msg.as_string())

s.quit()