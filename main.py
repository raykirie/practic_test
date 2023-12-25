
import logging
import unittest
from test_base import TestCRUDOperations

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCRUDOperations)
    unittest.TextTestRunner(verbosity=2).run(suite)
