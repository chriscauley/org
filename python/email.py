def send_email(from_,to='',cc='',bcc='',date='',subject='',body=''):
    if not to:
        raise Exception "You must specify a to address"
    lines = ["from: "+from_,
             "to: "+to,
             "subject: "+subject,
             "date: "+date,
             "cc: "+cc,
             "bcc: "+bcc,
             "",
             body]
    return '\n'.join(lines)

print send_email('chris@lablackey.com') #,'bob','','','today!',"I'm can't come in today","Because I'm too busy learning python")
