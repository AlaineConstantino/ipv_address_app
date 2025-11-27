# project_activity4_wow.py

presentation_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Project Activity 4 - Wow Presentation</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>
    body { margin:0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #111; color: #fff; overflow: hidden; }
    .slide { display: none; padding: 50px; height: 100vh; box-sizing: border-box; text-align: center; }
    .active { display: block; animation: fade 1s; }
    h1, h2 { color: #00FFAA; margin-bottom: 20px; text-shadow: 1px 1px 8px #0ff; }
    p, li { font-size: 1.2em; line-height: 1.6; }
    ul { list-style: none; padding: 0; }
    li { margin: 12px 0; }
    .icon { color: #00FFAA; margin-right: 10px; }
    .nav { position: fixed; bottom: 20px; width: 100%; text-align: center; }
    .nav button { padding: 10px 25px; font-size: 1em; border:none; border-radius: 5px; margin: 0 15px; cursor: pointer; background: #00FFAA; color: #111; transition: 0.3s; }
    .nav button:hover { background: #00cc88; color: #fff; }
    @keyframes fade { from {opacity: 0;} to {opacity: 1;} }
    .highlight { color: #FFD700; font-weight: bold; }
</style>
</head>
<body>

<div class="slide active">
    <h1><i class="fas fa-network-wired icon"></i>Project Activity 4</h1>
    <h2>Automated Software Testing & Deployment</h2>
    <p>Welcome to our WOW-factor presentation!</p>
</div>

<div class="slide">
    <h2><i class="fas fa-cogs icon"></i>A. Features Implemented</h2>
    <ul>
        <li><i class="fas fa-globe icon"></i>Automated IP information fetch (IPv4/IPv6)</li>
        <li><i class="fas fa-vial icon"></i>Automated testing using pytest</li>
        <li><i class="fas fa-code-branch icon"></i>CI/CD workflow simulation for commits</li>
    </ul>
</div>

<div class="slide">
    <h2><i class="fas fa-bullseye icon"></i>B. Objectives</h2>
    <ul>
        <li>Ensure IP info is fetched <span class="highlight">automatically</span> and accurately</li>
        <li>Catch code issues <span class="highlight">early</span> using automated testing</li>
        <li>Prevent broken commits using <span class="highlight">CI/CD best practices</span></li>
    </ul>
</div>

<div class="slide">
    <h2><i class="fas fa-lightbulb icon"></i>C. Why These Features</h2>
    <ul>
        <li>IP fetch is a core functionality of the application</li>
        <li>Automated testing improves reliability and saves debugging time</li>
        <li>CI/CD workflow ensures team productivity and code stability</li>
    </ul>
</div>

<div class="slide">
    <h2><i class="fas fa-users icon"></i>D. Team Member Roles & Skillsets</h2>
    <ul>
        <li>Alaine Nicole D. Constantino: Project Manager / Python Developer | Python, Git, CI/CD, DevOps basics</li>
        <li>Gracel Anne Belleca: Frontend Developer | HTML/CSS, UI design</li>
        <li>Johanna Anne De Pano: Backend Developer | Python, APIs</li>
        <li>Daryl Tumaneng: Tester / DevOps | Automated testing, GitHub Actions</li>
    </ul>
</div>

<div class="slide">
    <h2><i class="fas fa-project-diagram icon"></i>E. Project Strategy / Plan</h2>
    <ul>
        <li>Set up Python project structure</li>
        <li>Implement IP info functionality</li>
        <li>Write automated tests using pytest</li>
        <li>Simulate CI/CD pipeline using GitHub Actions</li>
        <li>Run and validate all tests before merging any code</li>
    </ul>
</div>

<div class="slide">
    <h2><i class="fas fa-check-circle icon"></i>F. Test Cases / Results</h2>
    <p><span class="highlight">2 test cases passed successfully</span> using pytest.</p>
</div>

<div class="slide">
    <h2><i class="fas fa-comments icon"></i>G. Team Activities & Reflections</h2>
    <ul>
        <li>Enjoyed collaborating and seeing automated testing catch issues early.</li>
        <li>Merge conflicts resolved using Git & careful commit reviews.</li>
        <li>Python import errors fixed by adjusting module paths.</li>
        <li>Accountability ensured via code review and testing.</li>
        <li>Consensus-based decision-making for major changes.</li>
        <li>Automated testing & CI/CD improved workflow efficiency.</li>
    </ul>
</div>

<div class="nav">
    <button onclick="prevSlide()">&#10094; Prev</button>
    <button onclick="nextSlide()">Next &#10095;</button>
</div>

<script>
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
    slides.forEach((s,i)=> s.classList.remove('active'));
    slides[index].classList.add('active');
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}
</script>

</body>
</html>
"""

with open("project_activity4_wow.html", "w") as f:
    f.write(presentation_html)

print("WOW Presentation generated: project_activity4_wow.html")
