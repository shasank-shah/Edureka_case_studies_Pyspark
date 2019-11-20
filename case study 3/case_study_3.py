import csv
import re
from Customer import Customer

class CustomerNotAllowedException(Exception):
    pass

def createOrder(_title, _firstName, _lastName, _isBlackListed):
    try:
        if _isBlackListed >= 1:
            raise CustomerNotAllowedException
        else:
            print(_title+' '+_firstName+' '+_lastName, "is not black listed")
    except CustomerNotAllowedException:
        print(_title + ' ' + _firstName + ' ' + _lastName, "is black listed")


with open('FairDealCustomerData.csv', 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    _lineCount = 0
    _title = ''
    _firstName = ''
    _lastName = ''
    for row in csv_reader:
        if _lineCount == 0:
            #print(row[1])
            _string = row[1]
            _isBlackListed = int(row[2])
            #print(_string)
            if '.' in _string:
                print(True)
                _title = (_string[slice(0, _string.find('.') + 1)])
                _string = _string[_string.find('.') + 1:].lstrip()
                #print(_title)
                #print(_string)
                _whiteSpaceCounter = 0
                for index in _string:
                    if (index.isspace()) == True:
                        #print("here")
                        _whiteSpaceCounter += 1
                #print(_whiteSpaceCounter)
                if _whiteSpaceCounter >= 1:
                    _firstName = (_string[slice(0, _string.find(' '))])
                    _string = _string[_string.find(' '):].lstrip()
                #print(_firstName)
                #print(_string)
                if _string != '':
                    _lastName = _string

                #print("The title is: ", _title, " and the first name is: ", _firstName, " and the last name is: ", _lastName, "asdadad")
                #print(_title + ' ' + _firstName + ' ' + _lastName)
                createOrder(_title, _firstName, _lastName, _isBlackListed)
            else:
                print(False)
                _whiteSpaceCounter = 0
                for index in _string:
                    if (index.isspace()) == True:
                        #print("here")
                        _whiteSpaceCounter += 1
                #print(_whiteSpaceCounter)
                if _whiteSpaceCounter >= 1:
                    _firstName = (_string[slice(0, _string.find(' '))])
                    _string = _string[_string.find(' '):].lstrip()
                #print(_firstName)
                #print(_string)
                if _string != '':
                    _lastName = _string

                #print("The title is: ", _title, " and the first name is: ", _firstName, " and the last name is: ", _lastName, "asdadad")
                #print(_firstName + ' ' + _lastName)
                createOrder(_title, _firstName, _lastName, _isBlackListed)