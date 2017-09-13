import csv
def ignore_char_from_string(my_string,char_in,char_in1):
    """ Remove Specific Char from the list"""
    my_string=my_string.replace(char_in,'')
    my_string=my_string.replace(char_in1,'')
    return my_string
class ParseFile(object):
    """
    This class has one list as its attribute and patient object
    """

    def __init__(self,filename):
        """
        initialize list of patients to empty list
        """
        self.filename=filename
        self.list_data = []
        self.row = 0
    def parse_file(self):
        """
        Opens a CSV file and filters it and save
        parsed results in list_data attribute of ParseFile
        """
        with open(self.filename, 'rb') as csv_file:
            reader = csv.reader(csv_file)
            for row_data in reader:
                if self.row > 0:
                    row_data[1]=float(ignore_char_from_string(row_data[1], '$',','))
                    self.list_data.append(row_data)
                self.row+=1
            csv_file.close()
            print(self.list_data)
    def calculate_amount(self,account):
        amount=0
        for row_data in self.list_data:
            if row_data[0]==account :
                amount-=row_data[1]
            if row_data[2]==account :
                amount+=row_data[1]
        
        print(amount)
        return amount

def my_script(filename,account):
    print(filename)
    input_file = ParseFile(filename)
    input_file.parse_file()
    return input_file.calculate_amount(account)
if __name__ == "__main__":
    print (lambda x,y: my_script(x,y))('transactions.csv','122')
