# scripts/allocate_funds.py

import numpy as np

def allocate_funds(proposals, total_funds):
    """
    Allocate funds to proposals based on their requested amounts.
    
    Args:
    proposals (list of dict): List of proposals with 'amount_requested' key.
    total_funds (float): Total funds available for allocation.
    
    Returns:
    list of dict: List of proposals with 'allocated_funds' key added.
    """
    # Sort proposals by requested amount in descending order
    proposals.sort(key=lambda x: x['amount_requested'], reverse=True)
    
    # Initialize allocated funds
    for proposal in proposals:
        proposal['allocated_funds'] = 0.0
    
    # Allocate funds
    remaining_funds = total_funds
    for proposal in proposals:
        if remaining_funds >= proposal['amount_requested']:
            proposal['allocated_funds'] = proposal['amount_requested']
            remaining_funds -= proposal['amount_requested']
        else:
            proposal['allocated_funds'] = remaining_funds
            remaining_funds = 0
    
    return proposals

# Test cases
def test_allocate_funds():
    proposals = [
        {'amount_requested': 5000},
        {'amount_requested': 3000},
        {'amount_requested': 2000},
        {'amount_requested': 1000}
    ]
    total_funds = 10000
    
    allocated_proposals = allocate_funds(proposals, total_funds)
    
    assert allocated_proposals[0]['allocated_funds'] == 5000
    assert allocated_proposals[1]['allocated_funds'] == 3000
    assert allocated_proposals[2]['allocated_funds'] == 2000
    assert allocated_proposals[3]['allocated_funds'] == 0
    
    print("All test cases passed!")

# Run test cases
test_allocate_funds()