class Customer:

    def __init__(self,name="",age="",gender="",phone_no="",email="",bmi="",duration=""):
        self.__name = name
        self.__age= age
        self.__gender = gender
        self.__phone_no = phone_no
        self.__bmi = bmi
        self.__duration = duration
        self.__email=email

    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setAge(self,age):
        self.__age = age
    
    def getAge(self):
        return self.__age

    def setGender(self,gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender
    
    def setPhone_no(self,phone_no):
        self.__phone_no=phone_no

    def getphone_no(self):
        return self.__phone_no

    def setEmail(self,email):
        self.__email=email

    def getEmail(self):
        return self.__email

    def setBmi(self,bmi):
         self.__bmi=bmi

    def getBmi(self):
        return self.__bmi

    def setDuration(self, duration):
        self.__duration=duration

    def getDuration(self):
        return self.__duration



    def __str__(self):
        return self.getName()+" "+self.getAge()+" "+self.getGender()+" "+self.getphone_no()+" "+self.getEmail()+" "+self.getBmi()+" "+self.getDuration()
