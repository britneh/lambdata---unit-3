import unittest
from britneh import add_state_names_column

class Testbritneh(unittest.TestCase):

    def test_add_state_names(self): #rename to function
        df = DataFrame({'abbrev': ['CT', 'CO', 'CA', 'TX']})
        #self.assertEqual('foo'.upper(), 'FOO')
        #invoke the function 
        self.assertEqual(len(df.columns), 1)
        self.assertEqual(list(df.columns), ['abbrev'])
        self.assertEqual(df.iloc[0]["abbrev"], 'CA')
   
        mapped_df = add_state_names_column(df)
        self.assertEqual(len(mapped_df.columns), 2)
        self.assertEqual(list(mapped_df.columns), ['abbrev', "name"])
        self.assertEqual(mapped_df.iloc[0]["abbrev"], 'CA')
        self.assertEqual(mapped_df.iloc[0]["name"], 'California')

if __name__ == '__main__':
    unittest.main() #invoking all of our test class'