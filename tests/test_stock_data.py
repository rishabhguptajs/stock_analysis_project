import unittest
import pandas as pd

class TestStockData(unittest.TestCase):
    
    def setUp(self):
        self.valid_data = pd.DataFrame({
            'Instrument': ['AAPL', 'GOOG'],
            'Date': pd.to_datetime(['2023-01-01', '2023-01-02']),
            'Open': [150.0, 100.0],
            'High': [155.0, 105.0],
            'Low': [148.0, 98.0],
            'Close': [152.0, 102.0],
            'Volume': [1000000, 1200000]
        })


    def test_valid_data(self):
        
        for col in ['Open', 'High', 'Low', 'Close']:
            self.assertTrue(pd.api.types.is_float_dtype(self.valid_data[col]))

        
        self.assertTrue(pd.api.types.is_integer_dtype(self.valid_data['Volume']))

        self.assertTrue(pd.api.types.is_string_dtype(self.valid_data['Instrument']))

        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.valid_data['Date']))


if __name__ == "__main__":
    unittest.main()