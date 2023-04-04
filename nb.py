from corpus import *
import numpy as np
import math


class spamfilter():
    def __init__(self):
        pass
    def train(self, emails):
        spam_count = {}
        ham_count = {}
        s_denominator = 0
        self.emails = emails
        for email in self.emails:
            if email[1] == 'spam':
                s_denominator += 1
                for word in email[0]:
                    if word not in spam_count:
                        spam_count[word] = 2
                    else:
                        spam_count[word] += 1
            elif email[1] == 'ham':
                for word in email[0]:
                    if word not in ham_count:
                        ham_count[word] = 2
                    else:
                        ham_count[word] += 1
 #smoothing
        for word in spam_count.keys():
            if word not in ham_count.keys():
                ham_count[word]=1
        for word in ham_count.keys():
            if word not in spam_count.keys():
                spam_count[word]=1
        
        
#division by the number of emails 
 
        spam_count={k:v/(s_denominator+1) for k, v in spam_count.items()}
        h_denominator=len(self.emails)-s_denominator
        ham_count={k:v/(h_denominator+1) for k, v in ham_count.items()}

        self.s_denominator=s_denominator
        self.h_denominator=h_denominator
        self.spam_count=spam_count
        self.ham_count=ham_count

    def classify(self,email_path):

        self.email_path=email_path
        email=readfile(self.email_path)
        spam_numbers=[]
        ham_numbers=[]

        
        for word in email:
            if word in self.spam_count.keys():
                spam_numbers.append(self.spam_count[word])
            if word in self.ham_count.keys():
                ham_numbers.append(self.ham_count[word])
            elif word not in self.ham_count.keys() and word not in self.spam_count.keys():
                spam_numbers.append(1/(self.s_denominator+1))
                ham_numbers.append(1/(self.h_denominator+1))


#logarithm
        
        log_spam_prod=np.sum([math.log(v) for v in spam_numbers])
        log_ham_prod=np.sum([math.log(v) for v in ham_numbers])
        log_ham_spam= np.logaddexp(log_spam_prod, log_ham_prod)
        spam_score=np.exp(log_spam_prod - log_ham_spam)

          
        if 0.5<spam_score<=1:
            return spam_score,'spam'
        elif 0<=spam_score<=0.5:
            return spam_score,'ham'
        else:
            return spam_score, 'error! system cannot categorize this email'  
        





