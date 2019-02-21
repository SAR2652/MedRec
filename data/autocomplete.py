import sqlite3

class DiseaseList:
    def __init__(self):
        self.conn = sqlite3.connect('medi_colab.db')
        self.c = self.conn.cursor()

    def generate_common_names_list(self):
        #accept common names output column from DB
        self.c.execute("""SELECT common_name FROM icd_codes""")
        names = self.c.fetchall()    #get output tuples
        common_names = []   #initialize an empty list

        #extract common names from output tuples into a list
        for common_name in names:
            common_names.append(common_name[0])

        return common_names
        
    def generate_scientific_names_list(self, name):
        #get icd_code for common_name
        self.c.execute("""SELECT icd_code WHERE common_name = {}""".format(name))



        