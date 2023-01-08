# Email-verify-API
Free basic email verify API

This API first checks if the email is in a valid format using a regular expression. It then verifies that the domain of the email exists by trying to resolve its DNS using the socket library. Finally, it attempts to verify the email address using an SMTP server. If any of these checks fail, the function returns False. Otherwise, it returns True.
