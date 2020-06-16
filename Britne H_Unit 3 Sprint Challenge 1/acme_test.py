import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_default_product_flame(self):
        """Test default product flammability being .5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flame, .5)    

    def test_explode_method(self):
        glove = BoxingGlove('Test Glove')
        self.assertEqual(glove.explode(), "...it's a glove.")

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Tests that report gives length 30"""
        gp = generate_products(30)
        self.assertEqual(len(gp), 30)


if __name__ == '__main__':
    unittest.main()
