#directory of namespace
dir(__builtins__)
'''
Dictionary are unuique and immutable
Global Namespace
Name (key) = 'exequiel' (value - can replace)

'''

Name = 'exequiel'

#print(Name)

class PlainWhiteMug:
    BaseColor = 'white'


edmontun_mug = PlainWhiteMug()
edmontun_mug.color = 'orange'
#########################################
#print(edmontun_mug.BaseColor)
#print(edmontun_mug.color )

###########################  Instance Attributes

class SampleClass:
    classAttrib = 1

    '''
    instance attritube
    allows to plugin parameters that be used to args
    adding default args to instance attri
    '''
    def __init__(self, Height=6, width=2):
        #Declaring instance attri na wala pang laman? Lalabas sa choices itong mga attri
        'same concept sa adding attrib to object'
        self.Height = Height
        self.width = width


kel_mug = SampleClass()

print(kel_mug.Height)

class ClassKel:
    class_attri = 100
    def __init__(self, height, length):
        self.height = height
        self.length = length

#    def __init__(self,item_name, base_price):


    def compute(self,height, length):
        size = (height * 2)/length
        print(f'Hello world {size}')
print(ClassKel)
obj1 = ClassKel(5,6)
obj2 = ClassKel(10000, 5000)

print(obj1.height)
print(obj2.height)

class TaxCompute:
    'Computes the applicable taxes and duties for a certain item'

    name = 'hello world'
    def __init__(self,item, base_price):
        """

        :param item:
        :param base_price:
        """
        self.item = item
        self.base_price = base_price

    def VatCompute(self):
        '''
        Computes for the VAT. It will return the 12% value of the Base Item Price
        :return:
        '''
        return self.base_price * .12

    def TotalPrice(self):
        '''
        Computes for the total of the Base price
        :return:
        '''
        return self.VatCompute() + self.base_price

    def DutyCompute(self,duty_percent):
        '''
        Initialized new attributes and computes Duty and Taxes
        :param duty_percent:
        :return:
        '''
        self.Duty = self.TotalPrice() * (duty_percent/100)
        self.TotalDuties = self.TotalPrice() + self.Duty
        return self.TotalDuties


    def Summary(self):
        '''
        print out the computations
        :return:
        '''
        print(f'Item Name = {self.item}')
        print(f'Base Price = {self.base_price}')
        print(f'VAT = {self.VatCompute()}')
        print(f'Duties = {self.Duty}')
        print(f'Total after Duties and Taxes = {self.DutyCompute(5)}')

help(TaxCompute)


'''object1 = TaxCompute('PS5', 27000)
object1.DutyCompute(5)
object1.Summary()
'''


class PrintMe:
    def __init__(self, fname, lname):
        self.fname = fname.split()
        self.lname = lname.split()

    def FullName(self):
        Cap_name = []

        name = ''
        for x in self.fname:
            y = x.capitalize()
            #Cap_name.append(y)
            name = name + y + ' '

        for x in self.lname:
            y = x.capitalize()
            #Cap_name.append(y)
            name = name + y + ' '

        #fullname = ' '.join(Cap_name)
        print(f'Hi {name}!')

Object1 = PrintMe('Paul john george ringo ELI RIVERMAYA', 'dela Cruz')
Object1.FullName()

class GetMe:
    def __init__(self, lowerlimit, upperlimit):
        self.lowerlimit = lowerlimit
        self.upperlimit = upperlimit

    def GetMeSum(self):
        sum1 = 0
        for num in range(self.upperlimit+1):
            sum1 += num
        return sum1

    def ProductGet(self):
        return self.lowerlimit * self.upperlimit

    def RangeSum(self):
        sum2 = 0
        for y in range(self.lowerlimit, self.upperlimit+1):
            sum2 += y
        return sum2

obj1 = GetMe(4,5)
print(obj1.GetMeSum())
print(obj1.ProductGet())
print(obj1.RangeSum())


class OddEven:
    def __init__(self, lowerlimit, upperlimit):
        self.lowerlimit = lowerlimit
        self.upperlimit = upperlimit

    def GetOdd(self):
        odd = []
        self.lower = self.lowerlimit

        if self.lowerlimit % 2 == 0:
            self.lower = self.lowerlimit + 1

        for x in range(self.lower, self.upperlimit+1, 2):
            odd.append(x)

        print(odd)
        print(f'There are {len(odd)} odd numbers from the range {self.lowerlimit}-{self.upperlimit}\n')

    def GetEven(self):
        even = []
        self.lowerEven = self.lowerlimit

        if self.lowerlimit % 2 != 0:
            self.lowerEven = self.lowerlimit + 1

        for y in range(self.lowerEven, self.upperlimit+1, 2):
            even.append(y)

        print(even)
        print(f'There are {len(even)} even numbers from the range {self.lowerlimit}-{self.upperlimit}\n')



obj1 = OddEven(6, 10)
obj1.GetOdd()
obj1.GetEven()

obj2 = OddEven(3, 21)
obj2.GetOdd()
obj2.GetEven()


class ClassKel:
    class_attri = 100
    def __init__(self, height, length):
        self.height = height
        self.length = length

#    def __init__(self,item_name, base_price):

    def ClassKel(self):
        print('hello world')
    def compute(self,height, length):
        size = (height * 2)/length
        print(f'Hello world {size}')

print(ClassKel)




































