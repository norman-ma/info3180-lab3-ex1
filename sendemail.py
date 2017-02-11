import smtplib

from_name = 'Michael-Anthony Norman'
from_addr = 'norman.michaelanthony@gmail.com'

to_name = 'Michael Norman'
to_addr = 'mikexcelsior@gmail.com'

subject = "Stuff You need to know"

msg = "Praesent vestibulum risus nec sem interdum, vitae tristique tortor consectetur. Pellentesque condimentum cursus quam vel lacinia. Aliquam et mattis quam. Suspendisse volutpat, felis at pretium lobortis, dolor erat condimentum velit, non hendrerit eros dolor in metus. Pellentesque pharetra dapibus libero, vel rutrum turpis aliquam sit amet. Aenean porta enim ante, quis pulvinar lorem aliquet et. In hac habitasse platea dictumst. Aliquam erat volutpat. Proin in Quisque sagittis ac enim et pulvinar. Pellentesque eu tincidunt velit. Cras ac est a massa iaculis condimentum. Curabitur a lorem posuere, convallis felis pulvinar, tempor justo. Mauris pellentesque lacus a erat sagittis volutpat. Suspendisse egestas dui eget sapien sodales pellentesque. Etiam volutpat tellus vitae pulvinar dapibus. Proin eget ornare purus. Integer ac neque ut dolor viverra ultricies. Phasellus eu nunc quis mauris consectetur ultricies vel nec nulla. Nulla ullamcorper et arcu vitae ultrices. Suspendisse ut sollicitudin augue, at aliquet metus. Ut ultrices varius accumsan. Sed lobortis, sapien vitae placerat dictum, dui lectus cursus orci, et molestie neque neque in tortor."

message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentials (if needed)
username = 'norman.michaelanthony@gmail.com'
password = 'xaocsiuyulfptjna'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()