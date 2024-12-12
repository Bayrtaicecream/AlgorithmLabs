import unittest  
import json  
from insertion import insertion_sort  
from binary import binary_search  
from merge import merge_sort 

def load_test_data(filename):
    with open(filename, 'r') as file: #zaa ene heseg ugaasaa oilgomjtoiii file aa read hiigeed hadgalnaa
        data = file.read() 
    lines = data.splitlines()    #mur muruur ni huvaaanaa 
    parsed_data = []      #ugugduluu hadgalah hooson jagsaalt
    for line in lines:  
        if line.strip(): #mur hooson bish bol urgegjilnee
            line = line.replace('][', ']\n[')      #hoorondoo ymar ch zaigui baival zuv formattai bolgoj ugnu
            line = line.strip() #strip ene bol taichih gazar gesen ug bishee ene bol functioooooon 
            # "Hello\nWorld\nTest" 
            #['hello', 'world', 'tesst']    #jishee ni ingej taslaj baigaa yumaa

            list_strings = line.split('\n') #muriig shine muruur huvaagad
            #hervee line olon murtei text baival list_string shine mur bolgoniig 1 element bolgoj jagsaaltad hadgalnaaa

            #end bolhoor ene chin json formattai baigaa bolhoor python object bolgoj baigaa yumaa
            list1 = json.loads(list_strings[0]) 
            list2 = json.loads(list_strings[1])
            #TUPLE
            parsed_data.append((list1, list2))  #tuple helbereer parsed_data ruu nemne
    return parsed_data
class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.test_data = load_test_data('/Users/nyam-osorbayrtaa/Desktop/Algo develop Lab/Lab-2/test.txt') 

    def test_insertion_sort(self):      #insersion sort algorithmniig testlex function
        all_correct = True           #shalgalt amjilttaa esehiig shalgah geed boolen huvisagch uusgeed
        for unsorted_list, sorted_list in self.test_data:     #eremblegdsen eremblegdeegui hoyulng ni 
            result = insertion_sort(unsorted_list)  #sortlogdoogui listee avch sortlood
            if result != sorted_list: #ali hediinee sortlogdson listee taarahgui baival ajilahgui baina gej uzeed break2
                all_correct = False #true false bolj baigaa biz naad nudeeree harda
                break  
        if all_correct: #tegeel end tegeel ajilaj baival urgegjleel yio bi odoo ene bolgoniig hurtel bichih ystoi yum baihda 
            print("insertion sort ajilaj baina")
            
        self.assertTrue(all_correct) 
        
    def test_merge_sort(self):
        all_correct = True  
        for unsorted_list, sorted_list in self.test_data: 
            result = merge_sort(unsorted_list) 
            if result != sorted_list: 
                all_correct = False  
                break 
        if all_correct:
            print("Merge sort ajilaj baina")     
        self.assertTrue(all_correct) 

    def test_binary_search(self): 
        all_correct = True 
        for unsorted_list, sorted_list in self.test_data: 
            sorted_list = sorted(unsorted_list) 
            ##################################
            #zaa binary bol zaaval eremblegdsen jagsaalt deer ajilnaaa
            for element in sorted_list:    #eremblegdsen jagsaalt deer binSear hiihiin tuld davt uusgenee

                # 0 : ali hesgees hailt ehleh
                # -1 : hasah 1 geheeree 0 ees hasah ni 1 gesen ugee tegheer hamgiin suul hurtel davtnaa
                #len(sorted_list) suuliin indexiig ilerhiilj baigaa ali hurtel hailt hiih hyzgaar geh yumu
                #element : jagsaalt dotroos oloh element
                index = binary_search(sorted_list, 0, len(sorted_list) - 1, element) 
                if index == -1 or sorted_list[index] != element:     #herev binSear element oldohgui baival -1 butsaadag
                    all_correct = False  
                    break  
            if not all_correct:  
                break  
        if all_correct:
            print("Binary ajilaj baina")
        self.assertTrue(all_correct)  
if __name__ == '__main__':
    unittest.main() 

