# scripts/extract_sdg_issues.py

import re
import json

def extract_sdg_issues(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    issues = []
    issue_pattern = re.compile(r'### Title: (.+?)\n### Description: (.+?)\n### submitter: (.+?)\n### project lead: (.+?)\n### Community benefit: (.+?)\n', re.DOTALL)

    for match in issue_pattern.findall(content):
        issue = {
            'title': match[0].strip(),
            'description': match[1].strip(),
            'submitter': match[2].strip(),
            'project_lead': match[3].strip(),
            'community_benefit': match[4].strip()
        }
        issues.append(issue)

    return issues

def save_issues_to_json(issues, output_file):
    with open(output_file, 'w') as file:
        json.dump(issues, file, indent=4)

if __name__ == "__main__":
    input_file = 'path/to/input/file.md'
    output_file = 'path/to/output/issues.json'
    issues = extract_sdg_issues(input_file)
    save_issues_to_json(issues, output_file)