from nb import *

nb=spamfilter()
nb.train(read_dataset(input('please enter the path to the training data directory')))
def read_batch(batch):
        result=[]
        import os
        emails_path=os.listdir(batch)
        for i in emails_path:
            complete_path=os.path.join(batch,i)
            result.append(nb.classify(complete_path))
        return result
querry=input('do you want to classify one email or a batch of emails? please answer one email or batch')
if querry=='one email':
    email_path=input('please enter the path to the email')
    print(nb.classify(email_path))
elif querry=='batch':
    batch_path=input('please enter the path to the batch file')
    print(read_batch(batch_path))
else:
    print('the input is wrong, please try again')
