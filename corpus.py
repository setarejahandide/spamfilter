
def tokenize(text):
    import nltk
    text=nltk.word_tokenize(text)
    return text


def readfile(path):
    word_lst=[]
    with open(path,encoding='utf-8',errors='ignore') as file:
        for line in file:
            line=tokenize(line)
            word_lst+=line
        word_lst = list(dict.fromkeys(word_lst))
    return word_lst



def read_dataset(path):
    import os 
    ham_path=os.path.join(path, 'ham')
    ham_lst=os.listdir(ham_path)

    all_emails=[]
    for i in ham_lst:
        if not i.startswith("."):
            i=os.path.join(ham_path, i)
            labelled_lst=(readfile(i),'ham')
            all_emails.append(labelled_lst)
    spam_path=os.path.join(path,'spam')
    spam_lst=os.listdir(spam_path)
    for i in spam_lst:
        if not i.startswith("."):
            i=os.path.join(spam_path, i)
            labelled_lst=(readfile(i),'spam')
            all_emails.append(labelled_lst)
    return all_emails








    




    
