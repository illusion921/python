#*_*coding:utf-8*_*
__author__ = 'smile'

account = {
    '1234':'smile',
    '1245':'yang',
    '6164':'illusion'
}
lock_information = {
    '1234':'0',
    '1245':'0',
    '6164':'0'
}
blance = {
    '1234' : '15000',
    '1245' : '15000',
    '6164' : '15000'
}
import pickle
#import json
#lk = open('lock.pkl','r+')
#pickle.dump(lock_information,lk)
#json.dump(lock_information,lk)
#lk.close()
#lk = open('lock.json','r+')
#b = pickle.load(lk)
#print b['1234']

def log_in():
    count = 0
    login = False
    while count < 3 and login != True:
        account_user = raw_input("Please input your account:").strip()

        if account_user in account.keys():
            lock_file = open('lock.pkl', 'r')
            b = pickle.load(lock_file)
            count = int(b[account_user])
            lock_file.close()
            while count < 3 and login != True:
                user_password = raw_input("Please input your password:").strip()
                if user_password == account[account_user]:
                    print "Successful user login!!!"
                    login = True
                    return 0
                else :
                    count += 1
                    continue
            if count == 3:
                print "Sorry...Your account is locked!!!"
                b [account_user] = '3'
                lock_file = open('lock.pkl', 'w')
                pickle.dump(b,lock_file)
                lock_file.close()
                return 1
        else :
            print "Please input correct account information!"
            continue
    '''
    if count == 3:
        print "Your account is locked!!!"
        unlock = raw_input("if you unlock your account,please input unlock:").strip()
        if unlock = "unlock":
            account_user = raw_input("Please input your account:").strip()
    '''

def unlock():
    while True:
        account_user = raw_input("Please input your account:").strip()
        if account_user in account.keys():
            lock_file = open('lock.pkl', 'r')
            b = pickle.load(lock_file)
            count = int(b[account_user])
            lock_file.close()
            if count !=3 :
                print "Your account is unlocked!!"
                break
            else :
                b[account_user] = '0'
                lock_file = open('lock.pkl', 'w')
                pickle.dump(b, lock_file)
                lock_file.close()
                print "Successful unlock accout!!"
                break
        else:
            print "Please input correct account information!"
            continue

def enchashment(account_user):
    cash = open('cash.pkl','r')
    b = pickle.load(cash)
    cash.close()

    while True:
        cash_num = raw_input("Please input enchashment!!").strip()
        if cash_num.isdigit():
            cash_num = int (cash_num)
            cash_num = int(b[account_user])-cash_num*1.05
            b[account_user] = cash_num
            cash = open('cash.pkl','w')
            pickle.dump(b,cash)
            cash.close()
            break
        else :
            print "Please input correct number!!"
            continue

def repayment(account_user):
    cash = open('cash.pkl', 'r')
    b = pickle.load(cash)
    cash.close()
    while True:
        cash_num = raw_input("Please input repayment!!").strip()
        if cash_num.isdigit():
            cash_num = int(cash_num)
            cash_num = int(b[account_user]) + cash_num
            b[account_user] = cash_num
            cash = open('cash.pkl', 'w')
            pickle.dump(b, cash)
            cash.close()
            print "Successful repayment"
            break
        else:
            print "Please input correct number!!"
            continue

def transfer_account(account_user1,account_user2):
    cash = open('cash.pkl', 'r')
    b = pickle.load(cash)
    cash.close()
    while True:
        cash_num1 = raw_input("Please input transfer_account!!").strip()
        if cash_num1.isdigit():
            cash_num1 = int(cash_num1)
            cash_num2 = int(b[account_user2]) + cash_num1
            cash_num1 = int(b[account_user1]) - cash_num1
            b[account_user2] = cash_num2
            b[account_user1] = cash_num1
            cash = open('cash.pkl', 'w')
            pickle.dump(b, cash)
            cash.close()
            print "Successful transfer_account"
            break
        else:
            print "Please input correct number!!"
            continue


#transfer_account('1234','6164')\
#enchashment('1234')
#log_in()
if __name__ == '__main__':
    log_in()