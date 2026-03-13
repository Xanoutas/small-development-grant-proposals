# scripts/allocate_funds.py

def allocate_funds(proposals, total_funds):
    """
    Allocate funds to proposals based on their requested amount.
    
    Args:
    proposals (list of dict): List of proposals with 'amount' key.
    total_funds (float): Total funds available for allocation.
    
    Returns:
    list of dict: List of proposals with 'allocated' key indicating the amount allocated.
    """
    # Sort proposals by requested amount in descending order
    proposals.sort(key=lambda x: x['amount'], reverse=True)
    
    # Allocate funds to proposals
    for proposal in proposals:
        if total_funds >= proposal['amount']:
            proposal['allocated'] = proposal['amount']
            total_funds -= proposal['amount']
        else:
            proposal['allocated'] = total_funds
            total_funds = 0
    
    return proposals

# scripts/test_allocate_funds.py

import unittest
from scripts.allocate_funds import allocate_funds

class TestAllocateFunds(unittest.TestCase):
    def test_allocate_funds(self):
        proposals = [
            {'amount': 5000},
            {'amount': 3000},
            {'amount': 2000},
            {'amount': 1000}
        ]
        total_funds = 8000
        
        expected_output = [
            {'amount': 5000, 'allocated': 5000},
            {'amount': 3000, 'allocated': 3000},
            {'amount': 2000, 'allocated': 0},
            {'amount': 1000, 'allocated': 0}
        ]
        
        self.assertEqual(allocate_funds(proposals, total_funds), expected_output)

    def test_allocate_funds_exact_match(self):
        proposals = [
            {'amount': 2000},
            {'amount': 3000},
            {'amount': 3000}
        ]
        total_funds = 8000
        
        expected_output = [
            {'amount': 2000, 'allocated': 2000},
            {'amount': 3000, 'allocated': 3000},
            {'amount': 3000, 'allocated': 3000}
        ]
        
        self.assertEqual(allocate_funds(proposals, total_funds), expected_output)

    def test_allocate_funds_insufficient_funds(self):
        proposals = [
            {'amount': 10000},
            {'amount': 5000}
        ]
        total_funds = 3000
        
        expected_output = [
            {'amount': 10000, 'allocated': 3000},
            {'amount': 5000, 'allocated': 0}
        ]
        
        self.assertEqual(allocate_funds(proposals, total_funds), expected_output)

if __name__ == '__main__':
    unittest.main()