import unittest
import router1


table_r1 = router1.read_csv("input/router_1_table.csv")
# A couple of simple tests to go thorugh basic behavior of overarching methods
class RouterTests(unittest.TestCase):
    def test_read_csv(self):
        self.assertEqual(5, len(table_r1))
        self.assertEqual(4, len(table_r1[0]))
        self.assertEqual(['0.0.0.0', '0.0.0.0', '127.0.0.1', '8002'], table_r1[0])
    
    def test_generate_forwarding_table_with_range(self):
        ftable_r1 = router1.generate_forwarding_table_with_range(table_r1)
        self.assertEqual(4, len(ftable_r1))
        self.assertEqual(4, len(ftable_r1[0]))
        self.assertEqual([167772352, 167772415, '127.0.0.1', '127.0.0.1'], ftable_r1[0])

if(__name__== '__main__'):
    unittest.main()