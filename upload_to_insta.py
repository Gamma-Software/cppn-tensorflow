import argparse
from instabot import Bot
import datetime

def get_first_file(passwd):
    import ftplib
    session = ftplib.FTP('mafreebox.freebox.fr')
    with open(passwd, "r") as f:
        session.login(f.readline().strip("\n"), f.readline().strip("\n"))
    session.cwd("PiValNas/abstract_art/to_upload")
    try:
        files = session.nlst()
    except ftplib.error_perm:
        session.quit()
        return None
    session.quit()
    if len(files) > 0:
        return files[0]
    else:
        return None

def delete_image(passwd):
    import ftplib
    session = ftplib.FTP('mafreebox.freebox.fr')
    with open(passwd, "r") as f:
        session.login(f.readline().strip("\n"), f.readline().strip("\n"))
    session.cwd("PiValNas/abstract_art/to_upload")
    try:
        files = session.nlst()
    except ftplib.error_perm:
        session.quit()
        return None
    session.delete(files[0])
    session.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Personal information')

    parser.add_argument('--passwd', dest='passwd', type=str, help='pass of the ftp logging')
    parser.add_argument('--passwd_insta', dest='passwd_insta', type=str, help='pass of the ftp logging')
    args = parser.parse_args()

    bot = Bot()
    with open(args.passwd_insta, "r") as f:
        bot.login(username = f.readline().strip("\n"), password = f.readline().strip("\n"))

    file_to_upload = get_first_file(args.passwd)

    if file_to_upload:
        import urllib.request as urllib2
        fh = urllib2.urlopen('ftp://server/path/file.png')
        open('file_to_upload.png', 'wb').write(fh.read())
        bot.upload_photo('file_to_upload.png', caption = "Daily dose of abstract art " + datetime.datetime.now().strftime("%Y_%m_%d"))
        delete_image(args.passwd)