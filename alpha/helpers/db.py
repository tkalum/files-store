import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate(
    {
  "type": "service_account",
  "project_id": "files-store-6d1df",
  "private_key_id": "3e146d43cde6f0ef08b45d2105be5ca28f6e78ac",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDG08/TgC6RalC7\np5waJRuuvqwqDNBd+kw77aZT22S3P/kqfZ+/RLTdlNhapKaE+vFtPcIgXLTx5BMm\nCpd4J/ftR0X/LpQEvQkzHgFgkG+eTGbjGpFpNjHrgIAHQoGIryoMUt4PyHoUjCcI\nfNzSs1fj97JbKZnuMuxwbZTN6cm21T2Bag+GXMkipcvfk+8QzOGWXOkbWM3Gz70I\nBTYl337/Uf7108cHHHYAeH6+ArlNOxd0DpdMf3G1+XSw8RSLDgSX2PkTNa5UM2+p\nK7rr05hYGFTEGeiMa/FdrP0c94N/DzmB9PkztPcdUctWD3NXf2jJ7dYWp+s4cVny\nhUQtgkFdAgMBAAECggEAMJhO1HzhBNoE+uRzlwFIU4yXNBzXJYz6KnCCZT77Tf2F\nBuFW1K70fK63NWpGJ7zUmpRMWNAHypIpqvPOQwgTxMrVfRHTjBfuwm9cO0959Gjs\ngae58ArWpx5MTFnxImjbgFEVpKplShXaKW0pJJdATT+6OCVCEdGg77actroj+rsT\nf3BHlHr8pWke98NCZc3Fcq3svcwUYSvSpoWUAQ+0cFFokQTYFwKjRXu5nkvy60zg\nLe51CuPCD6D5eyOJjC68yAdtMlWawoGNkuSD0aMLXlQ0c/IZbad2xmYWryMxnOp4\nnwp3d/6lK/ArAj6yG+zgmMYoS9MOUitFfBYbtb2nOQKBgQDyjkSzqV4mE/fti+dM\nowwuDXBRssXSIFzbN1xatbZMaCtbTLvJuG/cJRVQSCMF9M+xenpUH5WMh2Ow2WLZ\n8ifho0abKk04ieANzTittphS6fjViguL16NKDtO4GcNNXRyerh4THBScP6a0QSlC\nUOMT8iNvU7SH7XRrBEMuem08VQKBgQDR2Q/7dUK8QUlo7EcFSTn/q9LROpJx3O/j\n6ED2yiAzGPYcaWbcOOw2w9Vnt3GqzIOWe/PL/XgvqUGg6z/bWvusWL/RGhGVwdFx\n9EXkbkU7aUuTWJbie1I+/GX660nW5oc7N6W2lOTCqVIqaNrSjHdlYts1qxRfeTsy\nokTaWxT46QKBgB+bYmB3BYm4uGn//RgDdybZIXXD8fs7tF3sjOBVJXg3as7u5NmY\naxsoyeo4PDgeeqIJ777ejsJNMjRtX3A/GetRN3YowP9JGCU0RNp+HMNRMdfBsVd7\ntg+EdxpaYRTHuV8EGW8sDZN+x95dT18Q40ZKG0v6gF/mFXGMkKSR14IxAoGAdxDD\nGbkp2WjtvyO5FE29I80ZO/AQ4ZwrXNQN8Dk1VejG084WN8Pwew5YipWyX+fUjdDc\nvpSd2eUeQLDaNZsFC3/7rigtbBxhu1ePRJIwpAoVgJAWZID2ZJiPQHS6G74HYtkr\nJFKNDcpGvZtq9WYP5K3XlTbxw04lAZDComZlmukCgYBpTE3cOM2+sA1v5DaoBqfH\nrhPPFVUL/F2OR8TT5t9hKAQJdk46Y3fCIekgztPnjVLp9JkMT36gFpYBsLkloIeY\nW9Jl5LobDMGTbCqGl3PMiCvXxHn7cDH2/gW/UoaQjybOlRh6hy/P0ardgWXpAaLc\n39aA8dNtooHWdZ+UQWqz8A==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-yim4m@files-store-6d1df.iam.gserviceaccount.com",
  "client_id": "117195501795226329946",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-yim4m%40files-store-6d1df.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://files-store-6d1df-default-rtdb.firebaseio.com/'
})

# Main Ref
ref = db.reference('FilesStore/')

# Users and Groups
Grps = ref.child('Groups/')
Users = ref.child('Users/')

# All Users And Admins
All = Users.child('All/')
Admins = Users.child('Admins/')

# Data Ref
Data = ref.child('Data/')
Files = Data.child('Files/')
Movies = Data.child('Movies/')
Banned = Users.child('Banned')
MGroups = Data.child('AGroups/')
# Funcs
def AddmGroup(Title: str, ID: int):
    data = {ID: Title}
    MGroups.update(data)
    print(f'Added {Title} to Database')

def AddGroup(Title: str, ID: int):
    data = {ID: Title}
    Grps.update(data)
    print(f'Added {Title} to Database')

def AddUser(ID: int ,USERNAME: int):
    data = {ID : USERNAME}
    All.update(data)


def AddAdmin(Username: str, ID: int):
    data = {ID: Username}
    Admins.update(data)
    print(f'Promoted User @{Username} As Admin')

def Ban(Reason: str, ID: int, Username: str):
    R = f'{Username}:{Reason}'
    data = {ID: R}
    Banned.update(data)
    print(f'Banned User @{Username}')
# Function to add movies
def AddMvs(Name: str, Details: dict):
    movies_data = Movies.get()
    if movies_data is None:
        movies_data = {}

    if Name in movies_data:
        count = 1
        while f'{Name} {count}' in movies_data:
            count += 1
        new_name = f'{Name} {count}'
        movies_data[new_name] = Details
        Movies.set(movies_data)
        print(f'Added Movie "{new_name}" to Database')
    else:
        movies_data[Name] = Details
        Movies.set(movies_data)
        print(f'Added Movie "{Name}" to Database')

# Usage:

def GetUsers():
    data = All.get()
    return data

def GetMvs():
    data = Movies.get()
    return data

def Addfiles(Title: str, ID: int):
    data = {
    Title : {
        "Title" : Title,
        "Id" : ID,
    }
    }
    Files.update(data)


def Getfiles():
    data = Files.get()
    return data


