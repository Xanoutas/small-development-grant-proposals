# scripts/allocate_funds.py

import pandas as pd
import numpy as np

def allocate_funds(proposals, total_funds):
    """
    Allocate funds to proposals based on their priority and impact.
    
    Args:
    proposals (list of dict): List of proposals with keys 'name', 'priority', 'impact'.
    total_funds (float): Total funds available for allocation.
    
    Returns:
    dict: Allocated funds for each proposal.
    """
    # Convert proposals to DataFrame for easier manipulation
    df = pd.DataFrame(proposals)
    
    # Calculate total priority and impact scores
    total_priority = df['priority'].sum()
    total_impact = df['impact'].sum()
    
    # Normalize priority and impact scores
    df['priority_normalized'] = df['priority'] / total_priority
    df['impact_normalized'] = df['impact'] / total_impact
    
    # Calculate allocation based on normalized scores
    df['allocation'] = (df['priority_normalized'] + df['impact_normalized']) / 2
    
    # Scale allocations to total funds
    df['funds'] = df['allocation'] * total_funds
    
    # Convert DataFrame back to dictionary
    allocated_funds = df.to_dict(orient='records')
    
    return allocated_funds

# Example usage
proposals = [
    {'name': 'Dev Status Page', 'priority': 8, 'impact': 9},
    {'name': 'Identity Management System', 'priority': 7, 'impact': 8},
    {'name': 'Hubs Ingestion Platform', 'priority': 6, 'impact': 7},
    {'name': 'bioc2u', 'priority': 5, 'impact': 6},
    {'name': 'webR/RWASM', 'priority': 4, 'impact': 5}
]
total_funds = 100000

allocated_funds = allocate_funds(proposals, total_funds)
print(allocated_funds)