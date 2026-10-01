import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove "Master's Thesis" tab
html = html.replace('<span class="badge">Master&rsquo;s Thesis</span>\n', '')
html = html.replace('            <span class="badge">Master&rsquo;s Thesis</span>', '')
html = html.replace('<span class="badge">Master&rsquo;s Thesis</span>', '')

# 2. Remove "Academic Project" tabs
html = html.replace('<span class="badge">Academic Project</span>\n', '')
html = html.replace('            <span class="badge">Academic Project</span>\n', '')
html = html.replace('            <span class="badge">Academic Project</span>', '')
html = html.replace('<span class="badge">Academic Project</span>', '')

# 3. Extract projects to swap
# The projects-grid div contains the supporting projects.
# Let's split by '<article class="card project-card"'
parts = html.split('<article class="card project-card')

# parts[0] is up to the start of project 2.
# parts[1] is Project 2
# parts[2] is Project 3
# parts[3] is Project 4
# parts[4] is Project 5
# parts[5] is Project 6

# Re-read properly to be safe, because Project 6 has `project-card--full`.
# Actually, the split will split on `<article class="card project-card" id="supermarkets"` and `<article class="card project-card project-card--full" id="bikes-bi"`

p2_pattern = re.compile(r'(<!-- PROJECT 02.*?)(?=<!-- PROJECT 03)', re.DOTALL)
p3_pattern = re.compile(r'(<!-- PROJECT 03.*?)(?=<!-- PROJECT 04)', re.DOTALL)
p6_pattern = re.compile(r'(<!-- PROJECT 06.*?)(?=    </div><!-- /projects-grid -->)', re.DOTALL)

p2_match = p2_pattern.search(html)
p6_match = p6_pattern.search(html)

if p2_match and p6_match:
    p2_content = p2_match.group(1)
    p6_content = p6_match.group(1)
    
    # We need to swap them.
    # We also need to change the numbers and classes.
    # In p6_content (now becoming project 02):
    # Change "PROJECT 06" to "PROJECT 02"
    # Change "proj-num">06<" to "proj-num">02<"
    # Remove " project-card--full"
    # Remove "(full width)"
    
    new_p2_content = p6_content.replace('PROJECT 06', 'PROJECT 02')
    new_p2_content = new_p2_content.replace('<span class="proj-num">06</span>', '<span class="proj-num">02</span>')
    new_p2_content = new_p2_content.replace(' project-card--full', '')
    new_p2_content = new_p2_content.replace(' (full width)', '')

    # In p2_content (now becoming project 06):
    # Change "PROJECT 02" to "PROJECT 06"
    # Change "proj-num">02<" to "proj-num">06<"
    # Add " project-card--full" to the class
    # Add "(full width)" to the comment
    
    new_p6_content = p2_content.replace('PROJECT 02', 'PROJECT 06')
    new_p6_content = new_p6_content.replace('<span class="proj-num">02</span>', '<span class="proj-num">06</span>')
    new_p6_content = new_p6_content.replace('class="card project-card"', 'class="card project-card project-card--full"')
    new_p6_content = new_p6_content.replace('PROJECT 06 — SMI SUPERMARKETS', 'PROJECT 06 — SMI SUPERMARKETS (full width)')
    
    # Now replace them in the HTML
    html = html.replace(p2_content, new_p2_content)
    html = html.replace(p6_content, new_p6_content)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Swap successful")
else:
    print("Could not match projects")
    print(f"P2: {bool(p2_match)}")
    print(f"P6: {bool(p6_match)}")
