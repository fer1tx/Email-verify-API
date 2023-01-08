import re
import smtplib
import socket

def verify_email(email):
  # First, check if the email is in a valid format
  if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    return False
  
  # Next, verify that the domain of the email exists
  domain = email.split('@')[1]
  try:
    # Use the python built-in 'socket' library to resolve the DNS of the domain
    socket.gethostbyname(domain)
  except socket.gaierror:
    return False
  
  # Finally, try to verify the email address using an SMTP server
  try:
    # Use the python built-in 'smtplib' library to connect to the SMTP server
    # of the domain and issue the 'VRFY' command to verify the email address
    with smtplib.SMTP(f'smtp.{domain}') as smtp:
      # Some SMTP servers may not support the VRFY command, in which case
      # we'll use the 'RCPT TO' command instead.
      try:
        smtp.vrfy(email)
      except smtplib.SMTPCommandError:
        smtp.mail('')  # Send an empty 'MAIL FROM' command
        code, message = smtp.rcpt(email)  # Send the 'RCPT TO' command
        if (code // 100) == 2:  # 2xx status code indicates success
          return True
        else:
          return False
    return True
  except (smtplib.SMTPServerDisconnected, smtplib.SMTPException, socket.error):
    return False

print(verify_email('example@gmail.com')) # True
print(verify_email('invalid_email')) # False
print(verify_email('example@nonexistentdomain.com')) # False
