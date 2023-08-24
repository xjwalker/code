# import some mailgun library or similar
from services.email.templates.email_template import EmailTemplate


class MailgunLib:
    """
    fake class to make this work.
    """
    def __init__(self):
        pass

    def send_email(self, to, template):
        pass


class SendEmail:

    def __init(self, mailgun_lib: MailgunLib) -> None:
        self._mailgun_lib = mailgun_lib

    def send_email(self, to: str, email_template: EmailTemplate):
        self._mailgun_lib.send_email(to, email_template)
