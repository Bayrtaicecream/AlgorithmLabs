import unittest
import json

from aaa import optimal_bst
class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        with open('/Users/nyam-osorbayrtaa/Desktop/Algo develop Lab/Lab-6/test5.json', 'r') as file:
            self.test_cases = json.load(file)['test_cases5']
        
        with open('/Users/nyam-osorbayrtaa/Desktop/Algo develop Lab/Lab-6/test5.json', 'r') as file:
            self.test_cases2 = json.load(file)['test_cases6']
        
        with open('/Users/nyam-osorbayrtaa/Desktop/Algo develop Lab/Lab-6/test5.json', 'r') as file:
            self.test_cases3 = json.load(file)['test_cases7']
        
        print("Setup complete, test cases loaded.")
    
    def test_lab6(self):
        for case in self.test_cases2:
            self.assertEqual(optimal_bst(case["keys"], case["freq"], len(case["keys"])), case["expected"])

unittest.main()