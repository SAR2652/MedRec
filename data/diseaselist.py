import sqlite3, os
path = 'C:/MedRec'
class DiseaseList:
    def __init__(self):
        self.conn = sqlite3.connect(path + '/databases/medi_colab.db')
        self.c = self.conn.cursor()

    def generate_common_names_list(self):
        #accept common names output column from DB
        self.c.execute("""SELECT * FROM icd_codes""")
        names = self.c.fetchall()    #get output tuples
        common_names = ['']   #initialize a list with an empty string

        #extract common names from output tuples into a list
        for common_name in names:
            name = common_name[0] + ' - ' + common_name[1]
            common_names.append(name)

        return common_names
        
    def generate_scientific_names_list(self, icd_code):
        #get icd_sub_code and sub disease name from common name
        self.c.execute("""SELECT * FROM icd_sub_codes WHERE icd_code = '{}'""".format(icd_code))
        return self.c.fetchall()

        




        