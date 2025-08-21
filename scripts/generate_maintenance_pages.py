#!/usr/bin/env python3
import os
import random
import textwrap
import datetime
import json
import hashlib

BASE_DIR = "/workspace"
OUTPUT_DIR = os.path.join(BASE_DIR, "maintenance_pages")
CONNECTOR_PATH = os.path.join(BASE_DIR, "index.html")
TUTORIAL_PATH = os.path.join(BASE_DIR, "tutorial.html")

random.seed(1337)

# 1) Data sources for variety
base_niches = [
	"AI Analytics", "Eco Delivery", "Fintech Wallet", "HealthTech Portal", "EdTech Classroom",
	"Travel Planner", "Food Ordering", "Gaming Platform", "Streaming Studio", "Social Network",
	"Music Discovery", "Bookstore", "Fitness Coach", "Yoga Studio", "Smart Home",
	"Crypto Exchange", "NFT Gallery", "SaaS Dashboard", "Project Management", "Bug Tracker",
	"Marketing Suite", "AdTech Optimizer", "CRM System", "Helpdesk", "Chat Platform",
	"Photo Editor", "Video Editor", "Podcast Host", "E-commerce Fashion", "E-commerce Electronics",
	"Event Ticketing", "Ticket Support", "Job Board", "Recruitment", "HR Suite",
	"Real Estate", "Interior Design", "Architecture Studio", "3D Printing", "Robotics Lab",
	"AR/VR Studio", "Cybersecurity", "Compliance Suite", "LegalTech", "InsurTech",
	"IoT Platform", "Drone Delivery", "Weather Service", "Newsroom", "Publishing Platform",
	"Knowledge Base", "Note Taking", "Mind Mapping", "Calendar", "Task Manager",
	"Time Tracking", "Invoicing", "Accounting", "Payments", "Banking",
	"Ride Sharing", "Car Rental", "Parking Finder", "Public Transit", "Logistics",
	"Warehouse Manager", "Inventory", "Point of Sale", "Restaurant POS", "Hotel Booking",
	"Flight Deals", "Travel Insurance", "Language Learning", "Translation Service", "Typing Tutor",
	"Code Hosting", "CI/CD", "Package Registry", "Monorepo Tools", "API Gateway",
	"Auth Service", "Feature Flags", "A/B Testing", "Observability", "Error Tracking",
	"Status Page", "Incident Response", "Alerting", "Mobile Banking", "Microloans",
	"Crowdfunding", "Donations", "Nonprofit Hub", "Community Forum", "Q&A Platform",
	"Knowledge Graph", "Semantic Search", "Vector DB", "ML Ops", "Data Lake",
	"ETL Pipeline", "Data Catalog", "BI Dashboard", "Heatmaps", "User Analytics",
	"Personal Finance", "Budget Planner", "Savings Goals", "Stock Trading", "Options Desk",
	"Crypto Wallet", "DEX Aggregator", "Yield Farming", "Carbon Offsets", "Sustainability",
	"Green Energy", "Solar Planner", "EV Charging", "Battery Monitor", "Space Weather",
	"Astronomy Hub", "Education LMS", "Virtual Classroom", "Exam Prep", "Scholarships",
	"Grants Portal", "Research Papers", "Clinical Trials", "Telemedicine", "Pharmacy",
	"Lab Reports", "Genomics", "Bioinformatics", "Pet Care", "Veterinary",
	"Baby Care", "Parenting", "Wedding Planner", "Event Decor", "Photography",
	"Catering", "Art Marketplace", "Craft Supplies", "DIY Tutorials", "Home Repair",
	"Garden Planner", "Plant Care", "Aquarium", "Bird Watching", "Hiking Trails",
	"Cycling Club", "Running Tracker", "Marathon Planner", "Surf Forecast", "Ski Resort",
	"Campgrounds", "RV Rentals", "Boat Sharing", "Sailing Club", "Fishing Spots"
]

modifiers = [
	"Cloud", "HQ", "Studio", "Pro", "X", "Prime", "Edge", "Next", "One", "Core",
	"Flow", "OS", "Lab", "Works", "Engine", "Hub", "Forge", "Nest", "Pilot", "Pulse"
]

# Generate 155 unique project names
project_names = []
used = set()
i = 0
while len(project_names) < 155 and i < 10000:
	base = random.choice(base_niches)
	mod = random.choice(modifiers)
	name = f"{base} {mod}"
	if name not in used:
		project_names.append(name)
		used.add(name)
	i += 1

# Fonts pool (Google Fonts)
font_pairs = [
	("Poppins:wght@300;400;600;700", "Poppins"),
	("Inter:wght@300;400;600;700", "Inter"),
	("Space+Grotesk:wght@300;400;600;700", "Space Grotesk"),
	("Nunito:wght@300;400;700;800", "Nunito"),
	("Manrope:wght@300;400;700;800", "Manrope"),
	("Outfit:wght@300;400;700;800", "Outfit"),
	("Rubik:wght@300;400;700;800", "Rubik"),
	("Sora:wght@300;400;600;700", "Sora"),
	("Urbanist:wght@300;400;700;800", "Urbanist"),
	("Mulish:wght@300;400;700;800", "Mulish"),
	("Kanit:wght@300;400;700;800", "Kanit"),
	("Bricolage+Grotesque:wght@300;400;700;800", "Bricolage Grotesque"),
]

# Icon sets pool
icon_css = [
	"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css",
	"https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css",
	"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css"
]

# Feature icons per set
fa_icons = ["fa-rocket", "fa-shield-halved", "fa-gauge-high", "fa-bolt", "fa-leaf", "fa-wand-magic-sparkles", "fa-heart", "fa-brain", "fa-gear", "fa-cloud"]
bi_icons = ["bi-lightning-charge-fill", "bi-shield-lock", "bi-speedometer2", "bi-rocket-takeoff", "bi-stars", "bi-heart-fill", "bi-cpu", "bi-cloud-fill", "bi-palette", "bi-gem"]
bx_icons = ["bx-rocket", "bx-shield-quarter", "bx-tachometer", "bx-bolt-circle", "bx-leaf", "bx-magic-wand", "bx-heart", "bx-brain", "bx-cog", "bx-cloud"]

# Layout variants
layout_variants = ["layout-a", "layout-b", "layout-c", "layout-d", "layout-e", "layout-f", "layout-g", "layout-h"]

# Color palettes
color_palettes = [
	{"primary":"#7C3AED","secondary":"#06B6D4","accent":"#F59E0B","bg":"linear-gradient(135deg,#0F172A,#1E293B)"},
	{"primary":"#22C55E","secondary":"#3B82F6","accent":"#F97316","bg":"linear-gradient(135deg,#0B1020,#131A2A)"},
	{"primary":"#F43F5E","secondary":"#8B5CF6","accent":"#10B981","bg":"linear-gradient(135deg,#0A0A0F,#12121B)"},
	{"primary":"#06B6D4","secondary":"#22D3EE","accent":"#6366F1","bg":"linear-gradient(135deg,#0C111C,#0B1220)"},
	{"primary":"#EAB308","secondary":"#F97316","accent":"#84CC16","bg":"linear-gradient(135deg,#111827,#0D1320)"},
	{"primary":"#3B82F6","secondary":"#22C55E","accent":"#F43F5E","bg":"linear-gradient(135deg,#0E1117,#111827)"}
]

# Sentences pool for unique copy
intro_leads = [
	"We are fine-tuning the experience you love.",
	"Big improvements are loading behind the scenes.",
	"We're refueling the engines for a smoother journey.",
	"Polishing pixels and optimizing performance.",
	"Upgrading our core systems for reliability and speed.",
	"Deploying fresh features and stability fixes.",
	"Brewing something extraordinary for you.",
]

value_props = [
	"Sharper performance across devices",
	"Secure-by-default architecture",
	"Cleaner, more intuitive navigation",
	"Real-time insights at your fingertips",
	"Greener, energy-conscious infrastructure",
	"Smarter personalization and recommendations",
	"Accessibility enhancements for everyone",
]

cta_texts = [
	"Get status alerts", "Read the changelog", "Contact support", "Follow on X", "Join beta waitlist"
]

contact_links = [
	{"label":"Status", "href":"#", "icon":"fa-traffic-light"},
	{"label":"Changelog", "href":"#", "icon":"fa-scroll"},
	{"label":"Support", "href":"#", "icon":"fa-life-ring"},
	{"label":"Docs", "href":"#", "icon":"fa-book"}
]


# Utilities

def slugify(name: str) -> str:
	return "-".join(
		''.join(c.lower() if c.isalnum() else '-' for c in name).split('-')
	)


def ensure_dir(path: str):
	os.makedirs(path, exist_ok=True)


def pick_icons(css_url: str):
	if "font-awesome" in css_url:
		return [f"fa {random.choice(fa_icons)}" for _ in range(4)]
	if "bootstrap-icons" in css_url:
		return [f"bi {random.choice(bi_icons)}" for _ in range(4)]
	return [f"bx {random.choice(bx_icons)}" for _ in range(4)]


def svg_logo_svg(primary: str, secondary: str) -> str:
	grad_id = f"g{random.randint(1000,9999)}"
	return f'''<svg xmlns="http://www.w3.org/2000/svg" width="140" height="40" viewBox="0 0 140 40" role="img" aria-label="Logo">
	<defs>
		<linearGradient id="{grad_id}" x1="0%" y1="0%" x2="100%" y2="100%">
			<stop offset="0%" stop-color="{primary}"/>
			<stop offset="100%" stop-color="{secondary}"/>
		</linearGradient>
	</defs>
	<g>
		<rect rx="10" width="40" height="40" fill="url(#{grad_id})"/>
		<circle cx="20" cy="20" r="10" fill="rgba(255,255,255,0.2)"/>
		<path d="M14 26 L20 10 L26 26 Z" fill="#fff" opacity="0.9"/>
		<text x="50" y="26" font-family="Inter, Poppins, sans-serif" font-size="18" font-weight="700" fill="#ffffff">{random.choice(["Nimbus","Nova","Pulse","Orbit","Aero","Flux"])}</text>
	</g>
</svg>'''


def svg_favicon_svg(primary: str, accent: str) -> str:
	grad_id = f"f{random.randint(1000,9999)}"
	return f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
	<defs>
		<radialGradient id="{grad_id}" cx="50%" cy="50%" r="50%">
			<stop offset="0%" stop-color="{accent}"/>
			<stop offset="100%" stop-color="{primary}"/>
		</radialGradient>
	</defs>
	<rect width="64" height="64" rx="16" fill="url(#{grad_id})"/>
	<path d="M20 42 L32 16 L44 42 Z" fill="#fff" opacity="0.9"/>
</svg>'''


def html_template(title: str, niche: str, desc: str, features: list, colors: dict, font_url: str, font_name: str, icon_url: str, layout: str, deadline_iso: str, code_hash: str):
	# Different hero shapes per layout
	return f"""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>{title} — Maintenance</title>
	<link rel="preconnect" href="https://fonts.googleapis.com"/>
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
	<link href="https://fonts.googleapis.com/css2?family={font_url}&display=swap" rel="stylesheet"/>
	<link rel="stylesheet" href="{icon_url}"/>
	<link rel="icon" type="image/svg+xml" href="favicon.svg"/>
	<link rel="stylesheet" href="styles.css?v={code_hash}"/>
	<script>
		window.MAINTENANCE_DEADLINE = "{deadline_iso}";
	</script>
</head>
<body class="{layout}">
	<header class="nav">
		<div class="nav__inner container">
			<a class="brand" href="#">
				<img src="logo.svg" alt="{niche} logo" width="140" height="40" />
			</a>
			<nav class="menu" aria-label="Primary">
				<button class="menu__toggle" aria-expanded="false" aria-controls="menu-list">
					<span class="menu__bar"></span><span class="menu__bar"></span><span class="menu__bar"></span>
					<span class="sr-only">Toggle menu</span>
				</button>
				<ul id="menu-list" class="menu__list">
					<li><a href="#overview">Overview</a></li>
					<li><a href="#changelog">Changelog</a></li>
					<li><a href="#status">Status</a></li>
					<li><a href="#contact">Contact</a></li>
				</ul>
			</nav>
		</div>
	</header>

	<main>
		<section class="hero container">
			<div class="hero__content">
				<h1 class="title">{niche} <span class="tag">Maintenance</span></h1>
				<p class="lead">{desc}</p>
				<div class="timer" role="timer" aria-live="polite">
					<div class="time"><span id="d">00</span><label>Days</label></div>
					<div class="time"><span id="h">00</span><label>Hours</label></div>
					<div class="time"><span id="m">00</span><label>Minutes</label></div>
					<div class="time"><span id="s">00</span><label>Seconds</label></div>
				</div>
				<div class="actions">
					<a class="btn primary" href="#status"><i class="fa fa-signal"></i> System Status</a>
					<a class="btn ghost" href="#changelog"><i class="fa fa-scroll"></i> Changelog</a>
				</div>
			</div>
			<div class="hero__art" aria-hidden="true">
				<div class="orb orb--1"></div>
				<div class="orb orb--2"></div>
				<div id="floaters"></div>
			</div>
		</section>

		<section id="overview" class="features container">
			<h2>What we're improving</h2>
			<ul class="feature-list">
				<li><i class="{features[0]}"></i> Enhanced reliability and uptime guarantees</li>
				<li><i class="{features[1]}"></i> Faster page loads and buttery-smooth transitions</li>
				<li><i class="{features[2]}"></i> Stronger security and privacy controls</li>
				<li><i class="{features[3]}"></i> Refined design with accessible components</li>
			</ul>
		</section>

		<section id="changelog" class="changelog container">
			<h2>Recent highlights</h2>
			<div class="cards">
				<article class="card">
					<h3>Performance Pass</h3>
					<p>Database indices and query plans tuned. Asset pipeline optimized for {niche.lower()} workloads.</p>
				</article>
				<article class="card">
					<h3>Security Sweep</h3>
					<p>Zero-trust defaults, rotated keys, and expanded observability across critical paths.</p>
				</article>
				<article class="card">
					<h3>Design Refresh</h3>
					<p>New typography system with {font_name}. Improved contrast and motion preferences.</p>
				</article>
			</div>
		</section>

		<section id="status" class="status container">
			<h2>Planned completion</h2>
			<p>Our current window targets the countdown above. Timelines can shift as we validate quality.</p>
		</section>

		<section id="contact" class="contact container">
			<h2>Stay in the loop</h2>
			<div class="cta-row">
				<a class="btn primary" href="#"><i class="fa fa-bell"></i> {random.choice(cta_texts)}</a>
				<a class="btn ghost" href="#"><i class="fa fa-envelope"></i> {random.choice(cta_texts)}</a>
			</div>
		</section>
	</main>

	<footer class="footer">
		<div class="container footer__inner">
			<p>© {datetime.datetime.utcnow().year} {title}. All rights reserved.</p>
			<ul class="social">
				<li><a href="#" aria-label="Twitter"><i class="fa fa-brands fa-x-twitter"></i></a></li>
				<li><a href="#" aria-label="GitHub"><i class="fa fa-brands fa-github"></i></a></li>
				<li><a href="#" aria-label="Discord"><i class="fa fa-brands fa-discord"></i></a></li>
			</ul>
		</div>
	</footer>

	<script src="script.js?v={code_hash}"></script>
</body>
</html>"""


def css_template(colors: dict, font_name: str):
	base = """:root {
	--color-primary: __PRIMARY__;
	--color-secondary: __SECONDARY__;
	--color-accent: __ACCENT__;
	--bg-gradient: __BG__;
}
* { box-sizing: border-box; }
html, body { height: 100%; }
body {
	margin: 0;
	font-family: '__FONT__', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
	color: #e5e7eb;
	background: var(--bg-gradient);
	background-attachment: fixed;
}
.container {
	width: 100%;
	max-width: 1100px;
	margin: 0 auto;
	padding: 0 20px;
}
.sr-only {
	position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}

.nav { position: sticky; top: 0; z-index: 50; background: rgba(10,12,20,0.6); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.06); }
.nav__inner { display: flex; align-items: center; justify-content: space-between; height: 64px; }
.menu__toggle { display: none; background: none; border: 0; cursor: pointer; }
.menu__bar { display: block; width: 22px; height: 2px; background: #fff; margin: 5px 0; border-radius: 2px; }
.menu__list { display: flex; gap: 24px; list-style: none; padding: 0; margin: 0; }
.menu__list a { color: #e5e7eb; text-decoration: none; opacity: 0.9; }
.menu__list a:hover { color: var(--color-secondary); }

.hero { display: grid; grid-template-columns: 1.1fr 0.9fr; align-items: center; min-height: calc(100vh - 64px); gap: 40px; }
.hero__content { padding: 40px 0; }
.title { font-size: 44px; line-height: 1.1; margin: 0 0 16px; }
.tag { display: inline-block; font-size: 14px; margin-left: 12px; padding: 4px 10px; border-radius: 999px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12); color: var(--color-accent); }
.lead { font-size: 18px; opacity: 0.9; margin-bottom: 24px; }
.timer { display: grid; grid-template-columns: repeat(4, minmax(80px, 1fr)); gap: 12px; margin: 24px 0; }
.time { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); padding: 16px; border-radius: 16px; text-align: center; }
.time span { display: block; font-size: 28px; font-weight: 700; color: var(--color-secondary); }
.time label { font-size: 12px; opacity: 0.8; }
.actions { display: flex; gap: 12px; margin-top: 8px; }
.btn { text-decoration: none; padding: 12px 16px; border-radius: 12px; display: inline-flex; align-items: center; gap: 10px; border: 1px solid rgba(255,255,255,0.15); }
.btn.primary { background: var(--color-primary); color: #0a0c14; border-color: transparent; }
.btn.ghost { background: rgba(255,255,255,0.05); color: #fff; }

.hero__art { position: relative; min-height: 420px; }
.orb { position: absolute; filter: blur(10px); opacity: 0.8; }
.orb--1 { width: 220px; height: 220px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, var(--color-secondary), transparent 60%); top: -20px; right: -10px; animation: float1 6s ease-in-out infinite; }
.orb--2 { width: 180px; height: 180px; border-radius: 50%; background: radial-gradient(circle at 70% 70%, var(--color-accent), transparent 60%); bottom: -10px; left: 20px; animation: float2 7s ease-in-out infinite; }
#floaters span { position: absolute; display: block; border-radius: 50%; pointer-events: none; mix-blend-mode: screen; }
@keyframes float1 { from { transform: translateY(0px); } 50% { transform: translateY(-18px);} to { transform: translateY(0px);} }
@keyframes float2 { from { transform: translateY(0px); } 50% { transform: translateY(-14px);} to { transform: translateY(0px);} }

.features { padding: 48px 0; }
.features h2 { font-size: 24px; margin-bottom: 20px; }
.feature-list { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(220px, 1fr)); gap: 16px; }
.feature-list i { color: var(--color-accent); margin-right: 10px; }

.changelog { padding: 20px 0 48px; }
.cards { display: grid; grid-template-columns: repeat(3, minmax(220px, 1fr)); gap: 16px; }
.card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 16px; }

.status, .contact { padding: 20px 0 48px; }
.cta-row { display: flex; gap: 12px; flex-wrap: wrap; }

.footer { border-top: 1px solid rgba(255,255,255,0.08); padding: 24px 0; background: rgba(10,12,20,0.5); }
.footer__inner { display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.footer .social { list-style: none; margin: 0; padding: 0; display: flex; gap: 12px; }
.footer .social a { color: #cbd5e1; opacity: 0.9; }
.footer .social a:hover { color: var(--color-secondary); }

/* Layout variants tweak */
.layout-b .orb--1 { right: auto; left: -20px; }
.layout-c .cards { grid-template-columns: repeat(2, minmax(220px, 1fr)); }
.layout-d .feature-list { grid-template-columns: repeat(1, 1fr); }
.layout-e .hero { grid-template-columns: 1fr; }
.layout-f .title { font-size: 50px; }
.layout-g .timer { grid-template-columns: repeat(2, minmax(100px, 1fr)); }
.layout-h .btn.primary { background: var(--color-accent); color: #0a0c14; }

/* Responsive nav */
@media (max-width: 860px) {
	.menu__toggle { display: inline-flex; }
	.menu__list { position: absolute; right: 20px; top: 64px; background: rgba(10,12,20,0.95); border: 1px solid rgba(255,255,255,0.1); padding: 14px; border-radius: 12px; display: none; flex-direction: column; gap: 12px; }
	.menu__list.open { display: flex; }
	.hero { grid-template-columns: 1fr; }
	.cards { grid-template-columns: 1fr; }
}
"""
	return base.replace("__PRIMARY__", colors['primary']) \
		.replace("__SECONDARY__", colors['secondary']) \
		.replace("__ACCENT__", colors['accent']) \
		.replace("__BG__", colors['bg']) \
		.replace("__FONT__", font_name)


def js_template():
	return """(function(){
	const qs = (s,el=document)=>el.querySelector(s);
	const qsa = (s,el=document)=>Array.from(el.querySelectorAll(s));

	// Menu toggle
	const toggle = qs('.menu__toggle');
	const list = qs('#menu-list');
	if (toggle && list) {
		toggle.addEventListener('click', ()=>{
			const isOpen = list.classList.toggle('open');
			toggle.setAttribute('aria-expanded', String(isOpen));
		});
	}

	// Countdown
	const d = qs('#d'), h = qs('#h'), m = qs('#m'), s = qs('#s');
	const target = new Date(window.MAINTENANCE_DEADLINE || Date.now()+86400000);
	function pad(n){ return n<10? '0'+n : String(n); }
	function tick(){
		const now = new Date();
		let ms = target - now;
		if (ms < 0) ms = 0;
		const days = Math.floor(ms/86400000);
		const hours = Math.floor(ms%86400000/3600000);
		const mins = Math.floor(ms%3600000/60000);
		const secs = Math.floor(ms%60000/1000);
		if(d) d.textContent = pad(days);
		if(h) h.textContent = pad(hours);
		if(m) m.textContent = pad(mins);
		if(s) s.textContent = pad(secs);
	}
	setInterval(tick, 1000); tick();

	// Floating particles
	const floaters = qs('#floaters');
	if (floaters) {
		const W = floaters.clientWidth || 360;
		const H = floaters.clientHeight || 360;
		const count = 14 + Math.floor(Math.random()*10);
		for (let i=0;i<count;i++){
			const el = document.createElement('span');
			const size = 6 + Math.random()*20;
			el.style.width = size+'px';
			el.style.height = size+'px';
			el.style.left = Math.random()*90 + '%';
			el.style.top = Math.random()*90 + '%';
			el.style.background = `radial-gradient(circle at 30% 30%, var(--color-secondary), transparent)`;
			const dur = 6 + Math.random()*8;
			el.animate([
				{ transform: 'translateY(0px)' },
				{ transform: 'translateY(-18px)' },
				{ transform: 'translateY(0px)' }
			], { duration: dur*1000, iterations: Infinity, easing: 'ease-in-out', delay: Math.random()*1000 });
			floaters.appendChild(el);
		}
	}
})();
"""


def connector_html(links: list):
	items = "\n".join([f"\t\t<a class=\"card\" href=\"{href}\" target=\"_blank\">{title}</a>" for title, href in links])
	base = """<!DOCTYPE html>
<html lang=\"en\">
<head>
	<meta charset=\"UTF-8\" />
	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
	<title>Maintenance Templates — Gallery (155)</title>
	<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/>
	<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
	<link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap\" rel=\"stylesheet\"/>
	<style>
		:root{ --bg:#0b1020; --card:#11182a; --muted:#8ea0c8; --pri:#60a5fa; }
		*{box-sizing:border-box}
		body{margin:0;font-family:Inter,system-ui;background:linear-gradient(135deg,#0b1020,#0c1426);color:#d9e2ff;}
		.header{position:sticky;top:0;background:rgba(10,12,20,.6);backdrop-filter:blur(10px);border-bottom:1px solid #1f2940;padding:14px 0}
		.container{max-width:1200px;margin:0 auto;padding:0 20px}
		.hrow{display:flex;justify-content:space-between;gap:12px;align-items:center}
		.search{flex:1}
		.search input{width:100%;padding:12px 14px;border-radius:10px;border:1px solid #1f2940;background:#0f1626;color:#d9e2ff}
		.grid{display:grid;grid-template-columns:repeat(4,minmax(220px,1fr));gap:14px;padding:20px 0 40px}
		.card{display:block;padding:16px;border-radius:14px;background:linear-gradient(180deg,#0f172a,#121a30);border:1px solid #1f2940;color:#cfe0ff;text-decoration:none}
		.card:hover{border-color:#2b3a5e;box-shadow:0 10px 24px rgba(0,0,0,.24)}
		.footer{border-top:1px solid #1f2940;padding:18px 0;background:rgba(10,12,20,.5)}
		@media(max-width:980px){.grid{grid-template-columns:repeat(2,1fr)}}
		@media(max-width:560px){.grid{grid-template-columns:1fr}}
	</style>
</head>
<body>
	<header class=\"header\">
		<div class=\"container hrow\">
			<h1 style=\"margin:0;font-size:20px\">Maintenance Templates — 155</h1>
			<div class=\"search\"><input id=\"q\" type=\"search\" placeholder=\"Search templates...\"/></div>
		</div>
	</header>
	<main class=\"container\">
		<div id=\"grid\" class=\"grid\">
__ITEMS__
		</div>
	</main>
	<footer class=\"footer\">
		<div class=\"container\"><small>Open a template in a new tab. All pages are pure HTML/CSS/JS.</small></div>
	</footer>
	<script>
	const q = document.getElementById('q');
	q.addEventListener('input',()=>{
		const term = q.value.toLowerCase();
		for(const a of document.querySelectorAll('#grid .card')){
			a.style.display = a.textContent.toLowerCase().includes(term) ? '' : 'none';
		}
	});
	</script>
</body>
</html>"""
	return base.replace("__ITEMS__", items)


def tutorial_html():
	return """<!DOCTYPE html>
<html lang=\"en\">
<head>
	<meta charset=\"UTF-8\" />
	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
	<title>How to Customize Maintenance Templates</title>
	<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/>
	<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
	<link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap\" rel=\"stylesheet\"/>
	<style>
		body{margin:0;font-family:Inter,system-ui,Arial;color:#0f172a;background:#f6f7fb}
		.header{background:#0f172a;color:#fff;padding:20px}
		.container{max-width:900px;margin:0 auto;padding:24px}
		.card{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:16px 18px;margin:14px 0}
		code,pre{background:#0f172a;color:#e2e8f0;padding:2px 6px;border-radius:6px}
		ol,ul{padding-left:20px}
		@media(max-width:560px){.container{padding:16px}}
	</style>
</head>
<body>
	<header class=\"header\"><h1 style=\"margin:0\">Customize Your Maintenance Pages</h1></header>
	<main class=\"container\">
		<p>Each template folder contains <code>index.html</code>, <code>styles.css</code>, <code>script.js</code>, <code>logo.svg</code>, and <code>favicon.svg</code>. All are pure HTML/CSS/JS, no frameworks.</p>
		<div class=\"card\">
			<h2>Change the Logo</h2>
			<ol>
				<li>Replace <code>logo.svg</code> with your own SVG, or edit the file directly.</li>
				<li>Keep the width/height reasonable (e.g., 140×40). The nav will scale automatically.</li>
			</ol>
		</div>
		<div class=\"card\">
			<h2>Update the Favicon</h2>
			<ol>
				<li>Replace <code>favicon.svg</code> in the same folder.</li>
				<li>Favicons are referenced in <code>index.html</code> with <code>&lt;link rel=\"icon\" type=\"image/svg+xml\" href=\"favicon.svg\"&gt;</code>.</li>
			</ol>
		</div>
		<div class=\"card\">
			<h2>Change the Countdown Target</h2>
			<ol>
				<li>Open <code>index.html</code>.</li>
				<li>Find the script that sets <code>window.MAINTENANCE_DEADLINE</code>.</li>
				<li>Set it to an ISO date, e.g., <code>2025-12-31T23:59:59Z</code>.</li>
			</ol>
			<p>Alternatively, in <code>script.js</code> replace how <code>target</code> is computed.</p>
		</div>
		<div class=\"card\">
			<h2>Reset the Countdown</h2>
			<p>Set <code>window.MAINTENANCE_DEADLINE</code> to a future date/time. If the timer reaches zero, it will stop at 00:00:00:00.</p>
		</div>
		<div class=\"card\">
			<h2>Change Colors and Background</h2>
			<p>Edit CSS variables at the top of <code>styles.css</code>:</p>
			<pre>:root {\n  --color-primary: #7C3AED;\n  --color-secondary: #06B6D4;\n  --color-accent: #F59E0B;\n  --bg-gradient: linear-gradient(135deg,#0F172A,#1E293B);\n}</pre>
		</div>
		<div class=\"card\">
			<h2>Change Title, Paragraphs, Icons, Elements</h2>
			<p>Open <code>index.html</code> and update the markup: the title is inside <code>&lt;h1 class=\"title\"&gt;</code>, the paragraph uses <code>.lead</code>, and features are a list inside <code>#overview</code>. Icons use CDN classes (Font Awesome / Boxicons / Bootstrap Icons).</p>
		</div>
		<div class=\"card\">
			<h2>Background Animations</h2>
			<p>Orbs are controlled by <code>.orb--1</code> and <code>.orb--2</code>. Small floating particles are created in <code>script.js</code>. Adjust counts, sizes, and speeds to your taste.</p>
		</div>
		<div class=\"card\">
			<h2>Mobile Menu</h2>
			<p>The hamburger toggles the <code>.menu__list</code>. It is fully keyboard-accessible.</p>
		</div>
	</main>
</body>
</html>"""


def main():
	ensure_dir(OUTPUT_DIR)
	links = []
	common_js = js_template()
	for idx, proj in enumerate(project_names, start=1):
		niche = proj
		slug = slugify(niche)
		folder = os.path.join(OUTPUT_DIR, f"{idx:03d}-{slug}")
		ensure_dir(folder)
		# Select assets
		font_url, font_name = random.choice(font_pairs)
		icon_url = random.choice(icon_css)
		palette = random.choice(color_palettes)
		layout = random.choice(layout_variants)
		# Unique content
		lead = random.choice(intro_leads)
		benefit = random.choice(value_props)
		desc = f"{lead} Expect {benefit} tailored for {niche.lower()}."
		features = pick_icons(icon_url)
		# Unique deadline: between 1 and 40 days + random hours
		delta_days = random.randint(1, 40)
		delta_hours = random.randint(0, 23)
		deadline = (datetime.datetime.utcnow() + datetime.timedelta(days=delta_days, hours=delta_hours)).replace(microsecond=0)
		deadline_iso = deadline.isoformat() + "Z"
		# Cache bust hash
		code_hash = hashlib.md5(f"{niche}{deadline_iso}{layout}{font_url}".encode()).hexdigest()[:8]

		# Write files
		with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
			f.write(html_template(niche, niche, desc, features, palette, font_url, font_name, icon_url, layout, deadline_iso, code_hash))
		with open(os.path.join(folder, "styles.css"), "w", encoding="utf-8") as f:
			f.write(css_template(palette, font_name))
		with open(os.path.join(folder, "script.js"), "w", encoding="utf-8") as f:
			f.write(common_js)
		with open(os.path.join(folder, "logo.svg"), "w", encoding="utf-8") as f:
			f.write(svg_logo_svg(palette['primary'], palette['secondary']))
		with open(os.path.join(folder, "favicon.svg"), "w", encoding="utf-8") as f:
			f.write(svg_favicon_svg(palette['primary'], palette['accent']))

		rel = os.path.relpath(os.path.join(folder, "index.html"), BASE_DIR)
		links.append((niche, rel))

	# Write connector and tutorial
	with open(CONNECTOR_PATH, "w", encoding="utf-8") as f:
		f.write(connector_html(links))
	with open(TUTORIAL_PATH, "w", encoding="utf-8") as f:
		f.write(tutorial_html())

	print(json.dumps({"generated": len(project_names), "output_dir": OUTPUT_DIR, "connector": CONNECTOR_PATH, "tutorial": TUTORIAL_PATH}))


if __name__ == "__main__":
	main()