import subprocess

# ------------------------------
# Project Activity 4 Report
# ------------------------------

def print_section(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title) + "\n")

# 1. Features implemented
print_section("A. Features Implemented from Backlog")
features = [
    "Automated IP information fetch (IPv4/IPv6)",
    "Automated testing using pytest",
    "CI/CD workflow simulation for commits"
]
for f in features:
    print(f"- {f}")

# 2. Objectives
print_section("B. Objectives of These Features")
objectives = [
    "Ensure IP info is fetched automatically and accurately",
    "Catch code issues early using automated testing",
    "Prevent broken commits using CI/CD best practices"
]
for obj in objectives:
    print(f"- {obj}")

# 3. Why chosen
print_section("C. Why These Features Were Chosen")
reasons = [
    "IP fetch is a core functionality of the application",
    "Automated testing improves reliability and saves debugging time",
    "CI/CD workflow ensures team productivity and code stability"
]
for r in reasons:
    print(f"- {r}")

# 4. Team Roles and Skills
print_section("D. Team Member Roles and Skillsets")
team = [
    {"name": "Alaine Nicole D. Constantino", "role": "Project Manager / Python Developer", "skills": "Python, Git, CI/CD, DevOps basics"},
    {"name": "Gracel Anne Belleca", "role": "Frontend Developer", "skills": "HTML/CSS, UI design"},
    {"name": "Johanna Anne De Pano", "role": "Backend Developer", "skills": "Python, APIs"},
    {"name": "Daryl Tumaneng", "role": "Tester / DevOps", "skills": "Automated testing, GitHub Actions"}
]
for member in team:
    print(f"- {member['name']}: {member['role']} | Skills: {member['skills']}")

# 5. Project Strategy
print_section("E. Project Strategy / Plan")
strategy = [
    "Set up Python project structure",
    "Implement IP info functionality",
    "Write automated tests using pytest",
    "Simulate CI/CD pipeline using GitHub Actions",
    "Run and validate all tests before merging any code"
]
for s in strategy:
    print(f"- {s}")

# 6. Show test results (pytest)
print_section("F. Test Cases / Results")
try:
    # Run pytest in quiet mode and capture output
    result = subprocess.run(["pytest", "-q"], capture_output=True, text=True)
    print(result.stdout)
except Exception as e:
    print(f"Error running pytest: {e}")

# 7. Team Reflections
print_section("G. Team Activities and Reflections")

reflections = {
    "What we enjoyed": "Collaborating as a team and seeing automated testing catch issues early.",
    "Team problems and resolution": "Some merge conflicts; resolved using Git and careful commit reviews.",
    "Technical problems and resolution": "Initial Python import errors; fixed module paths and function signatures.",
    "Accountability": "Each member handled their tasks; code review and testing ensured team accountability.",
    "Decision-making": "Consensus-based; major changes discussed in team meetings.",
    "Team dynamics and lessons": "Good communication is key; automated testing and CI/CD improved workflow."
}

for question, answer in reflections.items():
    print(f"- {question}: {answer}")

print("\nProject Activity 4 Report Completed!\n")
