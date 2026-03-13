# scripts/allocate_funds.py

import pandas as pd
import numpy as np

def allocate_funds(proposals, total_funds):
    """
    Allocates funds to proposals based on their scores.
    
    Args:
    proposals (pd.DataFrame): DataFrame containing proposals with 'score' and 'budget' columns.
    total_funds (float): Total funds available for allocation.
    
    Returns:
    pd.DataFrame: DataFrame with updated 'allocated_funds' column.
    """
    # Sort proposals by score in descending order
    proposals = proposals.sort_values(by='score', ascending=False)
    
    # Initialize allocated funds column
    proposals['allocated_funds'] = 0.0
    
    # Calculate total budget requested
    total_requested_budget = proposals['budget'].sum()
    
    # If total requested budget is less than or equal to total funds, allocate fully
    if total_requested_budget <= total_funds:
        proposals['allocated_funds'] = proposals['budget']
    else:
        # Allocate funds proportionally based on scores
        remaining_funds = total_funds
        for index, row in proposals.iterrows():
            if remaining_funds <= 0:
                break
            allocation = min(row['budget'], remaining_funds)
            proposals.at[index, 'allocated_funds'] = allocation
            remaining_funds -= allocation
    
    return proposals

# Test cases
def test_allocate_funds():
    # Test case 1: Total requested budget <= total funds
    proposals = pd.DataFrame({
        'score': [0.8, 0.6, 0.4],
        'budget': [100, 100, 100]
    })
    total_funds = 300
    result = allocate_funds(proposals, total_funds)
    assert result['allocated_funds'].tolist() == [100, 100, 100]
    
    # Test case 2: Total requested budget > total funds
    proposals = pd.DataFrame({
        'score': [0.8, 0.6, 0.4],
        'budget': [100, 100, 100]
    })
    total_funds = 200
    result = allocate_funds(proposals, total_funds)
    assert result['allocated_funds'].tolist() == [100, 100, 0]
    
    # Test case 3: Unequal budget requests
    proposals = pd.DataFrame({
        'score': [0.8, 0.6, 0.4],
        'budget': [200, 100, 50]
    })
    total_funds = 300
    result = allocate_funds(proposals, total_funds)
    assert result['allocated_funds'].tolist() == [200, 100, 0]
    
    print("All test cases passed.")

# Run test cases
test_allocate_funds()