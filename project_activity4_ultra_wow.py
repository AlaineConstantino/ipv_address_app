# project_activity4_ultra_wow.py

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Project Activity 4 - Ultra Wow Presentation</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>
body { margin:0; font-family:'Segoe UI', sans-serif; background:#111; color:#fff; overflow:hidden; }
.slide { display:none; padding:50px; height:100vh; text-align:center; box-sizing:border-box; }
.active { display:block; animation:fade 1s; }
h1,h2 { color:#00FFAA; text-shadow:1px 1px 8px #0ff; margin-bottom:20px; }
p,li { font-size:1.2em; line-height:1.6; }
ul { list-style:none; padding:0; }
li { margin:12px 0; }
.icon { color:#00FFAA; margin-right:10px; }
.nav { position:fixed; bottom:20px; width:100%; text-align:center; }
.nav button { padding:10px 25px; font-size:1em; border:none; border-radius:5px; margin:0 15px; cursor:pointer; background:#00FFAA; color:#111; transition:0.3s; }
.nav button:hover { background:#00cc88; color:#fff; }
@keyframes fade { from {opacity:0;} to {opacity:1;} }
.card { display:inline-block; background:#222; padding:20px; margin:10px; border-radius:15px; box-shadow:0 0 20px #0ff; transition:0.5s; }
.card:hover { transform: scale(1.1); box-shadow:0 0 30px #FFD700; }
.progress { width:80%; background:#333; margin:10px auto; border-radius:20px; overflow:hidden; }
.progress-bar { height:25px; background:#00FFAA; width:0; transition:2s; }
.confetti { position: fixed; width: 100%; height: 100%; pointer-events:none; top:0; left:0; z-index:9999; }
</style>
</head>
<body>

<div class="slide active">
<h1><i class="fas fa-network-wired icon"></i>Project Activity 4</h1>
<h2>Ultra-Wow Presentation</h2>
<p>Dynamic live dashboard + animation effects!</p>
</div>

<div class="slide">
<h2><i class="fas fa-globe icon"></i>IP Info Dashboard</h2>
<div class="card"><i class="fas fa-globe-americas icon"></i>IPv4: 158.62.34.183</div>
<div class="card"><i class="fas fa-globe icon"></i>City: Quezon City</div>
<div class="card"><i class="fas fa-flag icon"></i>Country: Philippines</div>
<div class="card"><i class="fas fa-server icon"></i>ISP: Globe Telecom</div>
</div>

<div class="slide">
<h2><i class="fas fa-vial icon"></i>Automated Testing Status</h2>
<p>Simulated CI/CD Pipeline:</p>
<div class="progress"><div class="progress-bar" id="pipeline-bar"></div></div>
<p><span class="highlight">All tests passed!</span></p>
<canvas class="confetti" id="confetti"></canvas>
</div>

<div class="slide">
<h2><i class="fas fa-users icon"></i>Team & Roles</h2>
<div class="card">Alaine: Project Manager / Python Developer</div>
<div class="card">Gracel: Frontend Developer</div>
<div class="card">Johanna: Backend Developer</div>
<div class="card">Daryl: Tester / DevOps</div>
</div>

<div class="nav">
<button onclick="prevSlide()">&#10094; Prev</button>
<button onclick="nextSlide()">Next &#10095;</button>
</div>

<script>
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
function showSlide(i){slides.forEach((s,j)=>s.classList.remove('active')); slides[i].classList.add('active');}
function nextSlide(){currentSlide=(currentSlide+1)%slides.length; showSlide(currentSlide); if(currentSlide===2) animateProgress();}
function prevSlide(){currentSlide=(currentSlide-1+slides.length)%slides.length; showSlide(currentSlide);}

function animateProgress(){
    const bar = document.getElementById('pipeline-bar');
    bar.style.width = '100%';
    launchConfetti();
}

function launchConfetti(){
    const canvas = document.getElementById('confetti');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth; canvas.height = window.innerHeight;
    const confettiPieces = [];
    for(let i=0;i<150;i++){
        confettiPieces.push({x:Math.random()*canvas.width, y:Math.random()*canvas.height, r:Math.random()*6+4, d:Math.random()*10});
    }
    function draw(){
        ctx.clearRect(0,0,canvas.width,canvas.height);
        confettiPieces.forEach(p=>{
            ctx.fillStyle = `hsl(${Math.random()*360}, 100%, 50%)`;
            ctx.beginPath();
            ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
            ctx.fill();
            p.y+=p.d; if(p.y>canvas.height)p.y=0;
        });
        requestAnimationFrame(draw);
    }
    draw();
}
</script>

</body>
</html>
"""

with open("project_activity4_ultra_wow.html", "w") as f:
    f.write(html)

print("Ultra Wow Presentation generated: project_activity4_ultra_wow.html")
