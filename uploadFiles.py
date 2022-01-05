import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    for root, dirs, files in os.path
    relative_path=os.path.relpath(local_path, file_from)
    dropbox_path=os.path.join(file_to, relative_path)

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f= open(file_from, 'rb')
        dbx.files_upload(f.read(), dropbox_path, mode=WriteMode("overwrite"))

def main():
    access_token="XBxFT1Jy9VUAAAAAAAAAARYGY6VAh3sQiQefYjZxIviKQnjoBA4IQDGlBBwShket" 
    transferData = TransferData(access_token)
     
    file_from = input("enter the file path to transfer")
    file_to = ("C:\Users\ASUS\Dropbox\test")

    transferData.upload_file(file_from, file_to)
main()