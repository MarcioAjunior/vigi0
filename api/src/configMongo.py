from mongoengine import connect

def myConnection():
    try:
        connect(db = "vigi0", host= "mongodb+srv://admin:admin@devunc-marcio.lkpu4.mongodb.net/vigi0", alias="default")
    except Exception as e : 
        print(e)
        