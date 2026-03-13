# scripts/extract_sdg_issues.py

import os
import re
from bs4 import BeautifulSoup

def extract_sdg_issues_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    sdg_issues = []

    # Find all SDG issue sections
    sdg_sections = soup.find_all('div', class_='sdg-issue')
    for section in sdg_sections:
        issue_id = section.find('span', class_='issue-id').text.strip()
        issue_description = section.find('p', class_='issue-description').text.strip()
        sdg_issues.append({
            'id': issue_id,
            'description': issue_description
        })

    return sdg_issues

def save_sdg_issues_to_file(issues, file_path):
    with open(file_path, 'w') as file:
        for issue in issues:
            file.write(f"ID: {issue['id']}\nDescription: {issue['description']}\n\n")

def main():
    # Example HTML content (in a real scenario, this would be read from a file)
    html_content = """
    <div class="sdg-issue">
        <span class="issue-id">SDG-001</span>
        <p class="issue-description">This is the first SDG issue.</p>
    </div>
    <div class="sdg-issue">
        <span class="issue-id">SDG-002</span>
        <p class="issue-description">This is the second SDG issue.</p>
    </div>
    """

    # Extract SDG issues
    sdg_issues = extract_sdg_issues_from_html(html_content)

    # Save extracted issues to llms.txt
    llms_file_path = 'llms.txt'
    save_sdg_issues_to_file(sdg_issues, llms_file_path)
    print(f"SDG issues saved to {llms_file_path}")

    # Save extracted issues to llms-full.txt
    llms_full_file_path = 'llms-full.txt'
    with open(llms_full_file_path, 'w') as file:
        file.write(html_content)
    print(f"Full HTML content saved to {llms_full_file_path}")

if __name__ == "__main__":
    main()