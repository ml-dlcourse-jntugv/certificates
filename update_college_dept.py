import json
import csv

# Read the original data.csv with college and department info
college_dept_map = {}
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['1. Full Name (as to be printed on certificate)'].strip()
        college_dept_map[name] = {
            'college': row['  4. Name of the College'].strip(),
            'department': row['  3. Department'].strip()
        }

# Read the current data.json
with open('data.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# Update each entry with college and department
updated = 0
for cert_id, cert_data in data.items():
    name = cert_data['name'].strip()
    
    # Try to find matching name in college_dept_map
    if name in college_dept_map:
        cert_data['college'] = college_dept_map[name]['college']
        cert_data['department'] = college_dept_map[name]['department']
        updated += 1
        print(f"✓ Updated {cert_id}: {name}")
    else:
        print(f"⚠ No match found for: {name}")

# Write updated data back to data.json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"\n✅ Updated {updated} out of {len(data)} certificates")
print("data.json has been updated with college and department information")
