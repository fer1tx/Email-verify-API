import re
import smtplib

def verify_email(email):
  # First, check if the email is in a valid format
  if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    return False
  
  # Next, verify that the domain of the email exists
  domain = email.split('@')[1]
  try:
    # Use the python built-in 'socket' library to resolve the DNS of the domain
    socket.gethostbyname(domain)
  except socket.error:
    return False
  
  # Finally, try to verify the email address using an SMTP server
  try:
    smtp = smtplib.SMTP(f'smtp.{domain}')
    smtp.verify(email)
    return True
  except Exception:
    return False

print(verify_email('example@gmail.com')) # True
print(verify_email('invalid_email')) # False
print(verify_email('example@nonexistentdomain.com')) # False
