#!/usr/bin/env python3
import os
import random
import textwrap
import datetime
import json
import hashlib
import re

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


# ===================== THEMES =====================
# Each theme builder returns (html, css, js)

def build_theme(theme_key: str, ctx: dict):
	themes = {
		"aurora": theme_aurora,
		"neon_grid": theme_neon_grid,
		"glass_rings": theme_glass_rings,
		"light_progress": theme_light_progress,
		"terminal": theme_terminal,
		"waves": theme_waves,
		"stars": theme_stars,
		"mosaic": theme_mosaic,
		"sidebar_mesh": theme_sidebar_mesh,
		"vaporwave": theme_vaporwave,
	}
	return themes[theme_key](ctx)


def base_tokens(s: str, ctx: dict) -> str:
	# Replace common tokens in templates
	return (s.replace("__TITLE__", ctx['title'])
				.replace("__NICHE__", ctx['niche'])
				.replace("__DESC__", ctx['desc'])
				.replace("__YEAR__", str(ctx['year']))
				.replace("__FONT_URL__", ctx['font_url'])
				.replace("__FONT_NAME__", ctx['font_name'])
				.replace("__ICON_URL__", ctx['icon_url'])
				.replace("__DEADLINE__", ctx['deadline_iso'])
				.replace("__CODE_HASH__", ctx['code_hash'])
				.replace("__PRIMARY__", ctx['colors']['primary'])
				.replace("__SECONDARY__", ctx['colors']['secondary'])
				.replace("__ACCENT__", ctx['colors']['accent'])
				.replace("__BG__", ctx['colors']['bg']))


def features_list_html(icon_classes: list) -> str:
	lis = []
	texts = [
		"Enhanced reliability and uptime guarantees",
		"Faster page loads and buttery-smooth transitions",
		"Stronger security and privacy controls",
		"Refined design with accessible components",
	]
	for i in range(4):
		lis.append(f"<li><i class=\"{icon_classes[i]}\"></i> {texts[i]}</li>")
	return "\n\t\t\t\t" + "\n\t\t\t\t".join(lis)


# ---------- Theme: Aurora (orbs, baseline from earlier) ----------

def theme_aurora(ctx: dict):
	html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
	<meta charset=\"UTF-8\" />
	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
	<title>__TITLE__ — Maintenance</title>
	<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/>
	<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
	<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/>
	<link rel=\"stylesheet\" href=\"__ICON_URL__\"/>
	<link rel=\"icon\" type=\"image/svg+xml\" href=\"favicon.svg\"/>
	<link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
	<script>window.MAINTENANCE_DEADLINE = \"__DEADLINE__\";</script>
</head>
<body class=\"aurora\">
	<header class=\"nav\">
		<div class=\"nav__inner container\">
			<a class=\"brand\" href=\"#\"><img src=\"logo.svg\" alt=\"__NICHE__ logo\" width=\"140\" height=\"40\"/></a>
			<nav class=\"menu\" aria-label=\"Primary\">
				<button class=\"menu__toggle\" aria-expanded=\"false\" aria-controls=\"menu-list\"><span class=\"menu__bar\"></span><span class=\"menu__bar\"></span><span class=\"menu__bar\"></span><span class=\"sr-only\">Toggle menu</span></button>
				<ul id=\"menu-list\" class=\"menu__list\">
					<li><a href=\"#overview\">Overview</a></li>
					<li><a href=\"#changelog\">Changelog</a></li>
					<li><a href=\"#status\">Status</a></li>
					<li><a href=\"#contact\">Contact</a></li>
				</ul>
			</nav>
		</div>
	</header>
	<main>
		<section class=\"hero container\">
			<div class=\"hero__content\">
				<h1 class=\"title\">__NICHE__ <span class=\"tag\">Maintenance</span></h1>
				<p class=\"lead\">__DESC__</p>
				<div class=\"timer basic\" role=\"timer\" aria-live=\"polite\">
					<div class=\"time\"><span id=\"d\">00</span><label>Days</label></div>
					<div class=\"time\"><span id=\"h\">00</span><label>Hours</label></div>
					<div class=\"time\"><span id=\"m\">00</span><label>Minutes</label></div>
					<div class=\"time\"><span id=\"s\">00</span><label>Seconds</label></div>
				</div>
				<div class=\"actions\"><a class=\"btn primary\" href=\"#status\"><i class=\"fa fa-signal\"></i> System Status</a><a class=\"btn ghost\" href=\"#changelog\"><i class=\"fa fa-scroll\"></i> Changelog</a></div>
			</div>
			<div class=\"hero__art\" aria-hidden=\"true\"><div class=\"orb orb--1\"></div><div class=\"orb orb--2\"></div><div id=\"floaters\"></div></div>
		</section>
		<section id=\"overview\" class=\"features container\"><h2>What we're improving</h2><ul class=\"feature-list\">__FEATURES__</ul></section>
		<section id=\"changelog\" class=\"changelog container\">
			<h2>Recent highlights</h2>
			<div class=\"cards\"><article class=\"card\"><h3>Performance Pass</h3><p>Optimized for __NICHE__. Faster rendering and data fetching.</p></article><article class=\"card\"><h3>Security Sweep</h3><p>Upgraded auth flows and secrets rotation.</p></article><article class=\"card\"><h3>Design Refresh</h3><p>Typographic rhythm with __FONT_NAME__ and adaptive spacing.</p></article></div>
		</section>
		<section id=\"status\" class=\"status container\"><h2>Planned completion</h2><p>We aim to complete within the countdown window.</p></section>
		<section id=\"contact\" class=\"contact container\"><h2>Stay in the loop</h2><div class=\"cta-row\"><a class=\"btn primary\" href=\"#\"><i class=\"fa fa-bell\"></i> Get updates</a><a class=\"btn ghost\" href=\"#\"><i class=\"fa fa-envelope\"></i> Contact support</a></div></section>
	</main>
	<footer class=\"footer\"><div class=\"container footer__inner\"><p>© __YEAR__ __TITLE__. All rights reserved.</p><ul class=\"social\"><li><a href=\"#\" aria-label=\"Twitter\"><i class=\"fa fa-brands fa-x-twitter\"></i></a></li><li><a href=\"#\" aria-label=\"GitHub\"><i class=\"fa fa-brands fa-github\"></i></a></li><li><a href=\"#\" aria-label=\"Discord\"><i class=\"fa fa-brands fa-discord\"></i></a></li></ul></div></footer>
	<script src=\"script.js?v=__CODE_HASH__\"></script>
</body>
</html>"""
	css = css_template(ctx['colors'], ctx['font_name'])
	js = js_template()
	features_html = features_list_html(ctx['features'])
	return base_tokens(html.replace("__FEATURES__", features_html), ctx), css, js


# ---------- Theme: Neon Grid with flip clock ----------

def theme_neon_grid(ctx: dict):
	html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
	<meta charset=\"UTF-8\" />
	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
	<title>__TITLE__ — Maintenance</title>
	<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/>
	<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
	<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/>
	<link rel=\"stylesheet\" href=\"__ICON_URL__\"/>
	<link rel=\"icon\" type=\"image/svg+xml\" href=\"favicon.svg\"/>
	<link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
	<script>window.MAINTENANCE_DEADLINE = \"__DEADLINE__\";</script>
</head>
<body class=\"neon-grid\">
	<header class=\"topbar\"><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\" alt=\"logo\" width=\"140\" height=\"40\"/></a><button class=\"menu__toggle\" aria-expanded=\"false\">Menu</button></div></header>
	<aside class=\"drawer\" id=\"drawer\"><nav><a href=\"#overview\">Overview</a><a href=\"#changelog\">Changelog</a><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav></aside>
	<main class=\"container\">
		<section class=\"hero alt\">
			<h1>__NICHE__<span>Maintenance</span></h1>
			<p>__DESC__</p>
			<div class=\"flipclock\" aria-label=\"Timer\"><div class=\"fc\"><span id=\"fd\">00</span><label>Days</label></div><div class=\"fc\"><span id=\"fh\">00</span><label>Hours</label></div><div class=\"fc\"><span id=\"fm\">00</span><label>Min</label></div><div class=\"fc\"><span id=\"fs\">00</span><label>Sec</label></div></div>
			<div class=\"cta\"><a class=\"btn neon\" href=\"#status\">Live Status</a><a class=\"btn outline\" href=\"#changelog\">What changed</a></div>
		</section>
		<section id=\"overview\" class=\"panel\"><h2>Upgrades in progress</h2><ul class=\"grid features\">__FEATURES__</ul></section>
		<section id=\"changelog\" class=\"panel\"><h2>Highlights</h2><div class=\"grid cards\"><article><h3>Infra</h3><p>Autoscaling tuned and cold starts reduced.</p></article><article><h3>DX</h3><p>Cleaner APIs and faster build pipelines.</p></article><article><h3>UX</h3><p>Motion polished and settings streamlined.</p></article></div></section>
	</main>
	<footer class=\"grid-footer\"><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>
	<script src=\"script.js?v=__CODE_HASH__\"></script>
</body>
</html>"""
	css = """:root{--p:__PRIMARY__;--s:__SECONDARY__;--a:__ACCENT__;--bg:__BG__}
*{box-sizing:border-box}html,body{height:100%}body{margin:0;font-family:'__FONT_NAME__',system-ui;background:#050510;color:#d7e9ff}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
.topbar{position:sticky;top:0;background:rgba(5,5,16,.6);backdrop-filter:blur(10px);border-bottom:1px solid #1a1a2a}
.topbar .container{display:flex;justify-content:space-between;align-items:center;height:64px}
.menu__toggle{background:linear-gradient(90deg,var(--p),var(--s));color:#04040a;border:0;border-radius:10px;padding:8px 12px}
.drawer{position:fixed;left:-220px;top:64px;bottom:0;width:220px;background:#0b0b1a;border-right:1px solid #1a1a2a;padding:14px;transition:left .3s}
.drawer.open{left:0}
.drawer nav{display:flex;flex-direction:column;gap:10px}
.drawer a{color:#cfe0ff;text-decoration:none}
.hero.alt{padding:44px 0 14px;background-image:linear-gradient(180deg,rgba(124,58,237,.12),transparent),
	repeating-linear-gradient(0deg,rgba(96,165,250,.15) 0 2px,transparent 2px 40px),
	repeating-linear-gradient(90deg,rgba(99,102,241,.12) 0 2px,transparent 2px 40px)}
.hero.alt h1{font-size:48px;margin:0 0 8px}
.hero.alt h1 span{display:inline-block;font-size:14px;margin-left:10px;padding:4px 10px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);color:var(--a)}
.flipclock{display:grid;grid-template-columns:repeat(4,100px);gap:12px;margin:18px 0}
.fc{background:linear-gradient(180deg,#0d0d1e,#0b0b18);border:1px solid #20203a;border-radius:12px;padding:12px;text-align:center;box-shadow:0 6px 18px rgba(0,0,0,.3)}
.fc span{display:block;font-size:36px;font-weight:800;color:var(--s);transform-origin:bottom;}
.fc.flip span{animation:flip .6s ease}
@keyframes flip{0%{transform:rotateX(0)}50%{transform:rotateX(-70deg)}100%{transform:rotateX(0)}}
.grid.features{list-style:none;padding:0;margin:12px 0;display:grid;grid-template-columns:repeat(2,minmax(220px,1fr));gap:12px}
.grid.features li i{color:var(--a);margin-right:10px}
.panel{margin:20px 0}
.grid.cards{display:grid;grid-template-columns:repeat(3,minmax(220px,1fr));gap:12px}
.grid.cards article{background:rgba(255,255,255,.04);border:1px solid #222242;border-radius:12px;padding:14px}
.grid-footer{border-top:1px solid #1a1a2a;padding:18px 0;background:rgba(5,5,16,.5)}
@media(max-width:860px){.flipclock{grid-template-columns:repeat(2,1fr)}.grid.cards{grid-template-columns:1fr}}
"""
	js = """(function(){const q=s=>document.querySelector(s);const toggle=q('.menu__toggle');const drawer=q('#drawer');if(toggle&&drawer){toggle.addEventListener('click',()=>{drawer.classList.toggle('open')});}
const fd=q('#fd'),fh=q('#fh'),fm=q('#fm'),fs=q('#fs');const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);function pad(n){return n<10?'0'+n:String(n)};function set(el, val){if(!el)return;const prev=el.textContent;el.textContent=val;if(prev!==val){el.parentElement.classList.add('flip');setTimeout(()=>el.parentElement.classList.remove('flip'),600)}};function tick(){let ms=target-new Date();if(ms<0)ms=0;const d=Math.floor(ms/86400000);const h=Math.floor(ms%86400000/3600000);const m=Math.floor(ms%3600000/60000);const s=Math.floor(ms%60000/1000);set(fd,pad(d));set(fh,pad(h));set(fm,pad(m));set(fs,pad(s));}setInterval(tick,1000);tick();})();"""
	features_html = features_list_html(ctx['features']).replace('<li>','<li>').replace('</li>','</li>')
	return base_tokens(html.replace("__FEATURES__", features_html), ctx), base_tokens(css, ctx), js


# ---------- Theme: Glassmorphism with circular rings ----------

def theme_glass_rings(ctx: dict):
	html = """<!DOCTYPE html>
<html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/><title>__TITLE__ — Maintenance</title>
<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/>
<link rel=\"stylesheet\" href=\"__ICON_URL__\"/><link rel=\"icon\" type=\"image/svg+xml\" href=\"favicon.svg\"/>
<link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
<script>window.MAINTENANCE_DEADLINE=\"__DEADLINE__\";</script></head>
<body class=\"glass\"><div class=\"blur-bg\"></div>
<header class=\"nav glassbar\"><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\" alt=\"logo\"/></a><ul class=\"navlinks\"><li><a href=\"#overview\">Overview</a></li><li><a href=\"#status\">Status</a></li><li><a href=\"#contact\">Contact</a></li></ul></div></header>
<main class=\"container\"><section class=\"wrap\"><div class=\"copy\"><h1>__NICHE__</h1><p>__DESC__</p>
<div class=\"circle-timer\"><svg viewBox=\"0 0 180 180\" width=\"180\" height=\"180\"><circle class=\"bg\" cx=\"90\" cy=\"90\" r=\"80\"/><circle id=\"cd\" class=\"ring d\" cx=\"90\" cy=\"90\" r=\"80\"/><circle id=\"ch\" class=\"ring h\" cx=\"90\" cy=\"90\" r=\"64\"/><circle id=\"cm\" class=\"ring m\" cx=\"90\" cy=\"90\" r=\"48\"/><circle id=\"cs\" class=\"ring s\" cx=\"90\" cy=\"90\" r=\"32\"/></svg>
<div class=\"labels\"><div><span id=\"vd\">00</span><small>d</small></div><div><span id=\"vh\">00</span><small>h</small></div><div><span id=\"vm\">00</span><small>m</small></div><div><span id=\"vs\">00</span><small>s</small></div></div></div>
</div><div class=\"features glasscards\"><h2>Up next</h2><ul>__FEATURES__</ul></div></section></main>
<footer class=\"glassbar\"><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>
<script src=\"script.js?v=__CODE_HASH__\"></script></body></html>"""
	css = """:root{--p:__PRIMARY__;--s:__SECONDARY__;--a:__ACCENT__;--bg:__BG__}
body{margin:0;font-family:'__FONT_NAME__',system-ui;background:linear-gradient(135deg,#0b1020,#0c1426);color:#e6f0ff;}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
.blur-bg{position:fixed;inset:0;background:radial-gradient(1200px 600px at -10% -20%,rgba(96,165,250,.15),transparent),radial-gradient(900px 500px at 120% 20%,rgba(236,72,153,.15),transparent)}
.glassbar{backdrop-filter:blur(14px);background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-left:0;border-right:0}
.nav .container{display:flex;align-items:center;justify-content:space-between;height:64px}
.navlinks{display:flex;gap:16px;list-style:none;padding:0;margin:0}
.navlinks a{color:#dce8ff;text-decoration:none}
.wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:24px;min-height:calc(100vh - 120px);align-items:center}
.copy h1{font-size:48px;margin:0 0 6px;color:#fff}
.copy p{opacity:.92}
.circle-timer{position:relative;display:inline-grid;place-items:center}
.circle-timer svg{transform:rotate(-90deg)}
.circle-timer .bg{fill:none;stroke:rgba(255,255,255,.1);stroke-width:8}
.ring{fill:none;stroke-width:8;stroke-linecap:round}
.ring.d{stroke:var(--p)}.ring.h{stroke:var(--s)}.ring.m{stroke:var(--a)}.ring.s{stroke:#ffffff99}
.labels{position:absolute;display:grid;grid-template-columns:repeat(4,auto);gap:10px;bottom:-36px}
.labels div{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);padding:6px 10px;border-radius:10px}
.features.glasscards ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(2,minmax(220px,1fr));gap:12px}
.features.glasscards li i{color:var(--a);margin-right:10px}
footer{padding:18px 0;margin-top:10px}
@media(max-width:860px){.wrap{grid-template-columns:1fr}}
"""
	js = """(function(){function sel(s){return document.querySelector(s)};const C=Math.PI*2;function setRing(el,val,full){if(!el)return;const r=el.getAttribute('r');const L=2*Math.PI*r;el.setAttribute('stroke-dasharray',L);el.setAttribute('stroke-dashoffset',L*(1-val/full));}
const d=sel('#vd'),h=sel('#vh'),m=sel('#vm'),s=sel('#vs');const rd=sel('#cd'),rh=sel('#ch'),rm=sel('#cm'),rs=sel('#cs');const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);
function pad(n){return n<10?'0'+n:String(n)};function tick(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000);const H=Math.floor(ms%86400000/3600000);const M=Math.floor(ms%3600000/60000);const S=Math.floor(ms%60000/1000);
if(d)d.textContent=pad(D);if(h)h.textContent=pad(H);if(m)m.textContent=pad(M);if(s)s.textContent=pad(S);
setRing(rd, D%365, 365);setRing(rh,H,24);setRing(rm,M,60);setRing(rs,S,60);}setInterval(tick,1000);tick();})();"""
	features_html = features_list_html(ctx['features'])
	return base_tokens(html.replace("__FEATURES__", features_html), ctx), base_tokens(css, ctx), js


# ---------- Theme: Light with progress bars ----------

def theme_light_progress(ctx: dict):
	html = """<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<title>__TITLE__ — Maintenance</title><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/><link rel=\"stylesheet\" href=\"__ICON_URL__\"/>
<link rel=\"icon\" type=\"image/svg+xml\" href=\"favicon.svg\"/><link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
<script>window.MAINTENANCE_DEADLINE=\"__DEADLINE__\";</script></head>
<body class=\"light\"><header class=\"whitebar\"><div class=\"container\"><a href=\"#\" class=\"brand\"><img src=\"logo.svg\" alt=\"logo\"/></a><nav><a href=\"#overview\">Overview</a><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav></div></header>
<main class=\"container\"><section class=\"split\"><div class=\"col\"><h1>__NICHE__ Maintenance</h1><p>__DESC__</p>
<div class=\"bars\"><div class=\"bar\"><label>Days</label><div class=\"track\"><div id=\"pd\" class=\"fill\"></div></div><span id=\"vd\">0</span></div>
<div class=\"bar\"><label>Hours</label><div class=\"track\"><div id=\"ph\" class=\"fill\"></div></div><span id=\"vh\">0</span></div>
<div class=\"bar\"><label>Minutes</label><div class=\"track\"><div id=\"pm\" class=\"fill\"></div></div><span id=\"vm\">0</span></div>
<div class=\"bar\"><label>Seconds</label><div class=\"track\"><div id=\"ps\" class=\"fill\"></div></div><span id=\"vs\">0</span></div></div>
</div><div class=\"col art\"><div class=\"tile a\"></div><div class=\"tile b\"></div><div class=\"tile c\"></div></div></section>
<section id=\"overview\" class=\"list\"><h2>We're upgrading</h2><ul class=\"list\">__FEATURES__</ul></section></main>
<footer class=\"whitebar\"><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>
<script src=\"script.js?v=__CODE_HASH__\"></script></body></html>"""
	css = """body{margin:0;font-family:'__FONT_NAME__',system-ui;background:#f6f7fb;color:#0f172a}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
.whitebar{background:#fff;border-bottom:1px solid #e5e7eb}
.whitebar .container{display:flex;justify-content:space-between;align-items:center;height:64px}
.whitebar nav a{margin-left:14px;color:#0f172a;text-decoration:none}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:24px;min-height:calc(100vh - 120px);align-items:center}
.tile{height:120px;border-radius:16px;background:linear-gradient(135deg,rgba(124,58,237,.3),rgba(6,182,212,.3));box-shadow:0 10px 30px rgba(124,58,237,.15)}
.tile.b{transform:translateX(40px)}.tile.c{transform:translateX(20px)}
.bars{display:grid;gap:10px;margin-top:14px}
.bar{display:grid;grid-template-columns:80px 1fr 60px;gap:10px;align-items:center}
.track{height:10px;border-radius:999px;background:#e5e7eb;overflow:hidden}
.fill{height:100%;background:linear-gradient(90deg,__PRIMARY__,__SECONDARY__)}
.list{list-style:none;padding:0;margin:12px 0;display:grid;grid-template-columns:repeat(2,minmax(220px,1fr));gap:10px}
.list li i{color:__ACCENT__;margin-right:10px}
footer.whitebar{border-top:1px solid #e5e7eb;border-bottom:0;padding:16px 0}
@media(max-width:860px){.split{grid-template-columns:1fr}.bar{grid-template-columns:1fr 1fr 60px}}
"""
	js = """(function(){function q(s){return document.querySelector(s)};function w(el,val){if(!el)return;el.style.width=val+'%'};function t(el,txt){if(el)el.textContent=txt}
const pd=q('#pd'),ph=q('#ph'),pm=q('#pm'),ps=q('#ps');const vd=q('#vd'),vh=q('#vh'),vm=q('#vm'),vs=q('#vs');
const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);function pad(n){return n<10?'0'+n:String(n)}
function tick(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000);const H=Math.floor(ms%86400000/3600000);const M=Math.floor(ms%3600000/60000);const S=Math.floor(ms%60000/1000);
const pH=(H/24)*100,pM=(M/60)*100,pS=(S/60)*100;w(pd,Math.min(100,(D%30)/30*100));w(ph,pH);w(pm,pM);w(ps,pS);t(vd,pad(D));t(vh,pad(H));t(vm,pad(M));t(vs,pad(S));}
setInterval(tick,1000);tick();})();"""
	features_html = features_list_html(ctx['features'])
	return base_tokens(html.replace("__FEATURES__", features_html), ctx), base_tokens(css, ctx), js


# ---------- Theme: Terminal ----------

def theme_terminal(ctx: dict):
	html = """<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<title>__TITLE__ — Maintenance</title><link rel=\"icon\" type=\"image/svg+xml\" href=\"favicon.svg\"/><link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
<script>window.MAINTENANCE_DEADLINE=\"__DEADLINE__\";</script></head>
<body class=\"term\"><div class=\"scan\"></div><main class=\"termwrap\"><pre>> __TITLE__ maintenance window detected
> target: __NICHE__
> reason: rollout / tuning / security-hardening

$ uptime --expected
$ __COUNTDOWN__

$ notes
 - services partially unavailable
 - APIs return 503 for mutating operations
 - follow status page for updates
</pre></main><footer class=\"termfoot\">© __YEAR__ __TITLE__</footer>
<script src=\"script.js?v=__CODE_HASH__\"></script></body></html>"""
	css = """@font-face{font-family:Terminus;src:local('Courier New');}
body{margin:0;background:#020; color:#8f8; font-family:Terminus,monospace}
.termwrap{padding:20px;min-height:calc(100vh - 60px)}
pre{white-space:pre-wrap;line-height:1.6;text-shadow:0 0 8px #0f3}
.scan{position:fixed;inset:0;background:repeating-linear-gradient(0deg,rgba(0,255,128,.04) 0 2px,transparent 2px 6px),radial-gradient(circle at 50% -20%,rgba(0,255,128,.1),transparent);pointer-events:none}
.termfoot{border-top:1px solid #0a4;background:#010;padding:12px 20px}
"""
	js = """(function(){function q(s){return document.querySelector(s)};const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);
function fmt(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000);const H=Math.floor(ms%86400000/3600000);const M=Math.floor(ms%3600000/60000);const S=Math.floor(ms%60000/1000);
return D+'d '+H+'h '+M+'m '+S+'s';}
setInterval(()=>{const pre=q('pre');if(pre){pre.innerHTML=pre.innerHTML.replace(/\$ __COUNTDOWN__.*/,'$ __COUNTDOWN__ '+fmt())}},1000);})();"""
	return base_tokens(html, ctx), css, js


# ---------- Theme: Waves ----------

def theme_waves(ctx: dict):
	html = """<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<title>__TITLE__ — Maintenance</title><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/><link rel=\"stylesheet\" href=\"__ICON_URL__\"/><link rel=\"icon\" href=\"favicon.svg\"/>
<link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
<script>window.MAINTENANCE_DEADLINE=\"__DEADLINE__\";</script></head>
<body class=\"waves\"><svg class=\"bg\" viewBox=\"0 0 1440 320\"><path fill=\"__SECONDARY__\" fill-opacity=\"0.25\" d=\"M0,192L48,165.3C96,139,192,85,288,96C384,107,480,181,576,186.7C672,192,768,128,864,96C960,64,1056,64,1152,96C1248,128,1344,192,1392,224L1440,256L1440,0L1392,0C1344,0,1248,0,1152,0C1056,0,960,0,864,0C768,0,672,0,576,0C480,0,384,0,288,0C192,0,96,0,48,0L0,0Z\"></path></svg>
<header><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a><button id=\"m\">Menu</button><nav id=\"n\"><a href=\"#overview\">Overview</a><a href=\"#changelog\">Changelog</a><a href=\"#status\">Status</a></nav></div></header>
<main class=\"container\"><section class=\"hero\"><h1>__NICHE__</h1><p>__DESC__</p><div class=\"chips\"><span id=\"d\">00</span><span id=\"h\">00</span><span id=\"m\">00</span><span id=\"s\">00</span></div></section>
<section id=\"overview\" class=\"cards\"><h2>Focus areas</h2><ul class=\"cards\">__FEATURES__</ul></section>
</main><footer><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>
<script src=\"script.js?v=__CODE_HASH__\"></script></body></html>"""
	css = """body{margin:0;font-family:'__FONT_NAME__',system-ui;background:linear-gradient(180deg,#071426,#0b1c33);color:#e6efff}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
header{position:sticky;top:0;background:rgba(7,20,38,.6);backdrop-filter:blur(8px);border-bottom:1px solid #13243f}
header .container{display:flex;gap:12px;align-items:center;justify-content:space-between;height:64px}
#m{background:linear-gradient(90deg,__PRIMARY__,__SECONDARY__);border:0;color:#021024;padding:8px 12px;border-radius:10px}
#n{display:flex;gap:12px}
#n a{color:#d8e7ff;text-decoration:none}
.bg{position:fixed;left:0;right:0;bottom:0;z-index:-1}
.hero{min-height:40vh;padding:18px 0}
.chips span{display:inline-block;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:10px 12px;margin-right:8px;color:__SECONDARY__}
.cards{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(2,minmax(220px,1fr));gap:12px}
.cards li i{color:__ACCENT__;margin-right:10px}
footer{border-top:1px solid #13243f;padding:16px 0}
@media(max-width:860px){#n{display:none}.open #n{display:flex;flex-direction:column;position:absolute;right:20px;top:64px;background:#071426;border:1px solid #13243f;padding:12px;border-radius:12px}}
"""
	js = """(function(){const $=s=>document.querySelector(s);const m=$('#m'),n=$('#n');if(m){m.addEventListener('click',()=>{document.body.classList.toggle('open')});}
const d=$('#d'),h=$('#h'),m1=$('#m'),s=$('#s');const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);function pad(n){return n<10?'0'+n:String(n)};function tick(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);if(d)d.textContent=pad(D);if(h)h.textContent=pad(H);if(m1)m1.textContent=pad(M);if(s)s.textContent=pad(S);}setInterval(tick,1000);tick();})();"""
	features_html = features_list_html(ctx['features'])
	return base_tokens(html.replace("__FEATURES__", features_html), ctx), base_tokens(css, ctx), js


# ---------- Theme: Stars (canvas) with digital timer ----------

def theme_stars(ctx: dict):
	html = """<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<title>__TITLE__ — Maintenance</title><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/><link rel=\"stylesheet\" href=\"__ICON_URL__\"/>
<link rel=\"icon\" href=\"favicon.svg\"/><link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
<script>window.MAINTENANCE_DEADLINE=\"__DEADLINE__\";</script></head>
<body class=\"stars\"><canvas id=\"sky\"></canvas>
<header class=\"bar\"><div class=\"container\"><a href=\"#\" class=\"brand\"><img src=\"logo.svg\"/></a><nav><a href=\"#overview\">Overview</a><a href=\"#contact\">Contact</a></nav></div></header>
<main class=\"container\"><section class=\"center\"><h1>__NICHE__</h1><div class=\"digital\"><span id=\"d\">00</span>:<span id=\"h\">00</span>:<span id=\"m\">00</span>:<span id=\"s\">00</span></div><p>__DESC__</p></section>
<section id=\"overview\" class=\"tiles\"><h2>Upgrades</h2><ul>__FEATURES__</ul></section></main>
<footer class=\"bar\"><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>
<script src=\"script.js?v=__CODE_HASH__\"></script></body></html>"""
	css = """body{margin:0;font-family:'__FONT_NAME__',system-ui;background:#070818;color:#eaf2ff}
#sky{position:fixed;inset:0;z-index:-1}
.bar{background:rgba(7,8,24,.6);backdrop-filter:blur(8px);border-bottom:1px solid #171a3a}
.bar .container{display:flex;justify-content:space-between;align-items:center;height:64px}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
.center{min-height:40vh;display:grid;place-items:center;text-align:center;padding:30px 0}
.digital{font-variant-numeric:tabular-nums;font-weight:800;letter-spacing:2px;font-size:40px;color:__ACCENT__}
.tiles ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(3,minmax(220px,1fr));gap:12px}
.tiles li i{color:__SECONDARY__;margin-right:10px}
footer.bar{border-top:1px solid #171a3a;border-bottom:0;padding:14px 0}
@media(max-width:860px){.tiles ul{grid-template-columns:1fr}}
"""
	js = """(function(){const c=document.getElementById('sky');const ctx=c.getContext('2d');function resize(){c.width=innerWidth;c.height=innerHeight}addEventListener('resize',resize);resize();const stars=Array.from({length:180},()=>({x:Math.random()*c.width,y:Math.random()*c.height,z:Math.random()*2+.2}));function draw(){ctx.clearRect(0,0,c.width,c.height);for(const s of stars){ctx.fillStyle='rgba(255,255,255,'+(0.3+s.z/2)+')';ctx.fillRect(s.x,s.y,s.z,s.z);s.x+=0.05*s.z;if(s.x>c.width)s.x=0;}requestAnimationFrame(draw);}draw();
function q(s){return document.querySelector(s)};const d=q('#d'),h=q('#h'),m=q('#m'),s=q('#s');const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);function pad(n){return n<10?'0'+n:String(n)};function tick(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);if(d)d.textContent=pad(D);if(h)h.textContent=pad(H);if(m)m.textContent=pad(M);if(s)s.textContent=pad(S);}setInterval(tick,1000);tick();})();"""
	features_html = features_list_html(ctx['features'])
	return base_tokens(html.replace("__FEATURES__", features_html), ctx), base_tokens(css, ctx), js


# ---------- Theme: Mosaic grid ----------

def theme_mosaic(ctx: dict):
	html = """<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<title>__TITLE__ — Maintenance</title><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/><link rel=\"stylesheet\" href=\"__ICON_URL__\"/><link rel=\"icon\" href=\"favicon.svg\"/>
<link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
<script>window.MAINTENANCE_DEADLINE=\"__DEADLINE__\";</script></head>
<body class=\"mosaic\"><header class=\"hdr\"><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a><button id=\"t\">☰</button><ul id=\"ml\" class=\"ml\"><li><a href=\"#overview\">Overview</a></li><li><a href=\"#status\">Status</a></li><li><a href=\"#contact\">Contact</a></li></ul></div></header>
<main class=\"container\"><section class=\"tiles\"><div class=\"tile big\"></div><div class=\"tile\"></div><div class=\"tile\"></div><div class=\"tile\"></div><div class=\"tile\"></div></section>
<section class=\"content\"><h1>__NICHE__</h1><p>__DESC__</p><div class=\"badge-timer\"><span id=\"d\">0d</span><span id=\"h\">0h</span><span id=\"m\">0m</span><span id=\"s\">0s</span></div></section>
<section id=\"overview\" class=\"list\"><h2>Track</h2><ul class=\"list\">__FEATURES__</ul></section></main>
<footer class=\"hdr\"><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>
<script src=\"script.js?v=__CODE_HASH__\"></script></body></html>"""
	css = """body{margin:0;font-family:'__FONT_NAME__',system-ui;background:#0d0f16;color:#eaf1ff}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
.hdr{background:#0f1322;border-bottom:1px solid #1e2540}
.hdr .container{display:flex;align-items:center;justify-content:space-between;height:64px}
.ml{display:flex;gap:12px;list-style:none;margin:0;padding:0}
.ml a{color:#d8e6ff;text-decoration:none}
#t{background:#121833;color:#eaf1ff;border:1px solid #1e2540;border-radius:8px;padding:6px 10px}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:20px 0}
.tile{height:90px;border-radius:12px;background:linear-gradient(135deg,rgba(124,58,237,.3),rgba(6,182,212,.3))}
.tile.big{grid-column:span 2;height:190px}
.content{padding:16px 0}
.badge-timer span{display:inline-block;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);padding:6px 10px;border-radius:10px;margin-right:6px;color:__ACCENT__}
.list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(220px,1fr));gap:12px}
.list li i{color:__SECONDARY__;margin-right:10px}
footer.hdr{border-top:1px solid #1e2540;border-bottom:0;padding:14px 0}
@media(max-width:860px){.ml{display:none}.ml.open{display:flex;position:absolute;right:20px;top:64px;background:#0f1322;border:1px solid #1e2540;border-radius:12px;padding:12px;flex-direction:column}.tiles{grid-template-columns:repeat(2,1fr)}}
"""
	js = """(function(){const t=document.getElementById('t'),ml=document.getElementById('ml');if(t){t.addEventListener('click',()=>ml.classList.toggle('open'))}
function q(s){return document.querySelector(s)};const d=q('#d'),h=q('#h'),m=q('#m'),s=q('#s');const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);function tick(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);if(d)d.textContent=D+'d';if(h)h.textContent=H+'h';if(m)m.textContent=M+'m';if(s)s.textContent=S+'s';}setInterval(tick,1000);tick();})();"""
	features_html = features_list_html(ctx['features'])
	return base_tokens(html.replace("__FEATURES__", features_html), ctx), base_tokens(css, ctx), js


# ---------- Theme: Sidebar mesh ----------

def theme_sidebar_mesh(ctx: dict):
	html = """<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<title>__TITLE__ — Maintenance</title><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/><link rel=\"stylesheet\" href=\"__ICON_URL__\"/>
<link rel=\"icon\" href=\"favicon.svg\"/><link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
<script>window.MAINTENANCE_DEADLINE=\"__DEADLINE__\";</script></head>
<body class=\"sidebar\"><aside class=\"sidenav\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a><nav><a href=\"#overview\">Overview</a><a href=\"#changelog\">Changelog</a><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav></aside>
<main><section class=\"hero\"><h1>__NICHE__</h1><p>__DESC__</p><div class=\"rings\"><span id=\"d\">00</span><span id=\"h\">00</span><span id=\"m\">00</span><span id=\"s\">00</span></div></section>
<section id=\"overview\" class=\"grid\"><article><h3>Reliability</h3><p>Multi-region failover and graceful degradation.</p></article><article><h3>Security</h3><p>Least-privilege everywhere, better audit logs.</p></article><article><h3>Experience</h3><p>Cohesive theming and refined microinteractions.</p></article></section>
<footer><small>© __YEAR__ __TITLE__</small></footer></main>
<script src=\"script.js?v=__CODE_HASH__\"></script></body></html>"""
	css = """body{margin:0;font-family:'__FONT_NAME__',system-ui;background:radial-gradient(800px 400px at 10% 10%,rgba(124,58,237,.2),transparent),radial-gradient(800px 400px at 90% 90%,rgba(6,182,212,.2),transparent),#0c111b;color:#e7f1ff}
.sidenav{position:fixed;top:0;left:0;bottom:0;width:220px;background:#0f1626;border-right:1px solid #1a2640;padding:16px}
.sidenav nav{display:flex;flex-direction:column;gap:10px}
.sidenav a{color:#cfe0ff;text-decoration:none}
main{margin-left:220px}
.hero{min-height:40vh;padding:20px}
.rings span{display:inline-block;border:2px solid __SECONDARY__;color:__SECONDARY__;border-radius:999px;padding:10px 12px;margin-right:8px}
.grid{display:grid;grid-template-columns:repeat(3,minmax(220px,1fr));gap:12px;padding:20px}
.grid article{background:rgba(255,255,255,.04);border:1px solid #1a2640;border-radius:12px;padding:14px}
footer{border-top:1px solid #1a2640;padding:14px 20px;margin-left:220px}
@media(max-width:860px){.sidenav{position:static;width:auto;border-right:0}.sidenav nav{flex-direction:row;flex-wrap:wrap}.hero,footer{margin:0}main{margin:0}.grid{grid-template-columns:1fr}}
"""
	js = """(function(){function q(s){return document.querySelector(s)};const d=q('#d'),h=q('#h'),m=q('#m'),s=q('#s');const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);function pad(n){return n<10?'0'+n:String(n)};function tick(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);if(d)d.textContent=pad(D);if(h)h.textContent=pad(H);if(m)m.textContent=pad(M);if(s)s.textContent=pad(S);}setInterval(tick,1000);tick();})();"""
	return base_tokens(html, ctx), base_tokens(css, ctx), js


# ---------- Theme: Vaporwave ----------

def theme_vaporwave(ctx: dict):
	html = """<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<title>__TITLE__ — Maintenance</title><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
<link href=\"https://fonts.googleapis.com/css2?family=__FONT_URL__&display=swap\" rel=\"stylesheet\"/><link rel=\"stylesheet\" href=\"__ICON_URL__\"/>
<link rel=\"icon\" href=\"favicon.svg\"/><link rel=\"stylesheet\" href=\"styles.css?v=__CODE_HASH__\"/>
<script>window.MAINTENANCE_DEADLINE=\"__DEADLINE__\";</script></head>
<body class=\"vapor\"><header class=\"vw\"><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a><nav><a href=\"#overview\">Overview</a><a href=\"#contact\">Contact</a></nav></div></header>
<main class=\"container\"><section class=\"hero\"><h1><span>__NICHE__</span> is under maintenance</h1><p>__DESC__</p><div class=\"stripe-timer\"><div><label>Days</label><i id=\"d\" style=\"--v:0\"></i></div><div><label>Hours</label><i id=\"h\" style=\"--v:0\"></i></div><div><label>Minutes</label><i id=\"m\" style=\"--v:0\"></i></div><div><label>Seconds</label><i id=\"s\" style=\"--v:0\"></i></div></div></section>
<section id=\"overview\" class=\"v-cards\"><h2>Polishing</h2><ul>__FEATURES__</ul></section></main>
<footer class=\"vw\"><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>
<script src=\"script.js?v=__CODE_HASH__\"></script></body></html>"""
	css = """body{margin:0;font-family:'__FONT_NAME__',system-ui;background:linear-gradient(120deg,#1b1135,#25134a 40%,#0d3550);color:#f0e6ff}
.vw{background:linear-gradient(90deg,#ff71ce22,#01cdfe22,#05ffa122);border-bottom:1px solid #2a2050}
.vw .container{display:flex;justify-content:space-between;align-items:center;height:64px}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
.hero{min-height:40vh;padding:24px 0}
.hero h1 span{background:linear-gradient(90deg,#ff71ce,#01cdfe,#05ffa1);-webkit-background-clip:text;background-clip:text;color:transparent}
.stripe-timer{display:grid;grid-template-columns:repeat(2,minmax(220px,1fr));gap:12px;margin:18px 0}
.stripe-timer div{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:12px}
.stripe-timer i{display:block;height:10px;border-radius:10px;background:linear-gradient(90deg,__PRIMARY__,__SECONDARY__);width:calc(var(--v)*1%)}
.v-cards ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(3,minmax(220px,1fr));gap:12px}
.v-cards li i{color:__ACCENT__;margin-right:10px}
footer.vw{border-top:1px solid #2a2050;border-bottom:0;padding:14px 0}
@media(max-width:860px){.v-cards ul{grid-template-columns:1fr}}
"""
	js = """(function(){function q(s){return document.querySelector(s)};const d=q('#d'),h=q('#h'),m=q('#m'),s=q('#s');const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);function set(el,percent){if(el)el.style.setProperty('--v',percent)}function tick(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);set(d,(D%30)/30*100);set(h,(H/24)*100);set(m,(M/60)*100);set(s,(S/60)*100);}setInterval(tick,1000);tick();})();"""
	features_html = features_list_html(ctx['features'])
	return base_tokens(html.replace("__FEATURES__", features_html), ctx), base_tokens(css, ctx), js


# ---------- Unique per-template builder ----------

def build_unique_template(ctx: dict, salt: int):
	# Variant pools
	nav_variants = ["top","split","center","drawer","sidebar","bottom"]
	hero_variants = ["left","right","center","fullscreen"]
	features_variants = ["list","cards","steps","media"]
	timer_variants = ["blocks","flip","rings","bars","chips","digital","badges","stripes","text"]
	art_variants = ["orbs","waves","stars","mesh","blobs","noise","stripes","triangles"]
	footer_variants = ["simple","columns","center","social","mini"]

	random.seed(hash((ctx['title'], salt, ctx['code_hash'])) & 0xffffffff)
	nav = random.choice(nav_variants)
	hero = random.choice(hero_variants)
	feat = random.choice(features_variants)
	timer = random.choice(timer_variants)
	art = random.choice(art_variants)
	foot = random.choice(footer_variants)

	# Unique class suffix
	uid = hashlib.md5(f"{ctx['title']}-{salt}-{nav}-{hero}-{feat}-{timer}-{art}-{foot}".encode()).hexdigest()[:6]

	# Tokens
	tokens = {
		"UID": uid,
		"NAV": nav,
		"HERO": hero,
		"FEAT": feat,
		"TIMER": timer,
		"ART": art,
		"FOOT": foot,
	}

	# HTML pieces
	def nav_html():
		if nav == "top":
			return f"""
	<header class=\"nav-{uid} top\"><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\" width=\"140\" height=\"40\"/></a><nav class=\"links\"><a href=\"#overview\">Overview</a><a href=\"#changelog\">Changelog</a><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav><button class=\"burger\" aria-controls=\"menu\" aria-expanded=\"false\">☰</button></div><ul id=\"menu\" class=\"menu\"><li><a href=\"#overview\">Overview</a></li><li><a href=\"#status\">Status</a></li><li><a href=\"#contact\">Contact</a></li></ul></header>
	"""
		if nav == "split":
			return f"""
	<header class=\"nav-{uid} split\"><div class=\"container\"><nav class=\"left\"><a href=\"#overview\">Overview</a><a href=\"#changelog\">Changelog</a></nav><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a><nav class=\"right\"><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav></div></header>
	"""
		if nav == "center":
			return f"""
	<header class=\"nav-{uid} center\"><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a><nav class=\"links\"><a href=\"#overview\">Overview</a><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav></div></header>
	"""
		if nav == "drawer":
			return f"""
	<header class=\"nav-{uid} drawer\"><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a><button class=\"drawer-btn\" aria-controls=\"drawer\" aria-expanded=\"false\">Menu</button></div><aside id=\"drawer\" class=\"drawer-panel\"><nav><a href=\"#overview\">Overview</a><a href=\"#changelog\">Changelog</a><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav></aside></header>
	"""
		if nav == "sidebar":
			return f"""
	<aside class=\"nav-{uid} sidebar\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a><nav><a href=\"#overview\">Overview</a><a href=\"#changelog\">Changelog</a><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav></aside>
	"""
		# bottom
		return f"""
	<header class=\"nav-{uid} bottom\"><div class=\"container\"><a class=\"brand\" href=\"#\"><img src=\"logo.svg\"/></a></div></header>
	<nav class=\"bottombar\"><a href=\"#overview\">Overview</a><a href=\"#changelog\">Changelog</a><a href=\"#status\">Status</a><a href=\"#contact\">Contact</a></nav>
	"""

	def timer_html():
		# Different timers markup
		if timer == "blocks":
			return """
	<div class=\"timer blocks\" role=\"timer\"><div><span id=\"d\">00</span><label>Days</label></div><div><span id=\"h\">00</span><label>Hours</label></div><div><span id=\"m\">00</span><label>Minutes</label></div><div><span id=\"s\">00</span><label>Seconds</label></div></div>
	"""
		if timer == "flip":
			return """
	<div class=\"flipclock\"><div class=\"fc\"><span id=\"fd\">00</span><label>d</label></div><div class=\"fc\"><span id=\"fh\">00</span><label>h</label></div><div class=\"fc\"><span id=\"fm\">00</span><label>m</label></div><div class=\"fc\"><span id=\"fs\">00</span><label>s</label></div></div>
	"""
		if timer == "rings":
			return """
	<div class=\"rings\"><svg viewBox=\"0 0 180 180\"><circle class=\"bg\" cx=\"90\" cy=\"90\" r=\"80\"/><circle id=\"cd\" class=\"ring d\" cx=\"90\" cy=\"90\" r=\"80\"/><circle id=\"ch\" class=\"ring h\" cx=\"90\" cy=\"90\" r=\"64\"/><circle id=\"cm\" class=\"ring m\" cx=\"90\" cy=\"90\" r=\"48\"/><circle id=\"cs\" class=\"ring s\" cx=\"90\" cy=\"90\" r=\"32\"/></svg><div class=\"labels\"><span id=\"vd\">00</span><span id=\"vh\">00</span><span id=\"vm\">00</span><span id=\"vs\">00</span></div></div>
	"""
		if timer == "bars":
			return """
	<div class=\"bars\"><div class=\"bar\"><label>Days</label><i id=\"pd\"></i><span id=\"vd\">00</span></div><div class=\"bar\"><label>Hours</label><i id=\"ph\"></i><span id=\"vh\">00</span></div><div class=\"bar\"><label>Minutes</label><i id=\"pm\"></i><span id=\"vm\">00</span></div><div class=\"bar\"><label>Seconds</label><i id=\"ps\"></i><span id=\"vs\">00</span></div></div>
	"""
		if timer == "chips":
			return """
	<div class=\"chips\"><span id=\"d\">00</span><span id=\"h\">00</span><span id=\"m\">00</span><span id=\"s\">00</span></div>
	"""
		if timer == "digital":
			return """
	<div class=\"digital\"><span id=\"d\">00</span>:<span id=\"h\">00</span>:<span id=\"m\">00</span>:<span id=\"s\">00</span></div>
	"""
		if timer == "badges":
			return """
	<div class=\"badges\"><em id=\"d\">0d</em><em id=\"h\">0h</em><em id=\"m\">0m</em><em id=\"s\">0s</em></div>
	"""
		if timer == "stripes":
			return """
	<div class=\"stripes\"><div><label>Days</label><i id=\"sd\"></i></div><div><label>Hours</label><i id=\"sh\"></i></div><div><label>Minutes</label><i id=\"sm\"></i></div><div><label>Seconds</label><i id=\"ss\"></i></div></div>
	"""
		# text
		return """
	<p class=\"text-count\">Estimated time remaining: <strong id=\"td\">00</strong>d <strong id=\"th\">00</strong>h <strong id=\"tm\">00</strong>m <strong id=\"ts\">00</strong>s</p>
	"""

	def features_html():
		ic = ctx['features']
		if feat == "list":
			return f"<ul class=\"feat list\"><li><i class=\"{ic[0]}\"></i> Reliability upgrades</li><li><i class=\"{ic[1]}\"></i> Performance boosts</li><li><i class=\"{ic[2]}\"></i> Security hardening</li><li><i class=\"{ic[3]}\"></i> Design refinements</li></ul>"
		if feat == "cards":
			return f"""
	<div class=\"feat cards\"><article><i class=\"{ic[0]}\"></i><h3>Reliability</h3><p>Higher uptime targets.</p></article><article><i class=\"{ic[1]}\"></i><h3>Performance</h3><p>Faster interactions.</p></article><article><i class=\"{ic[2]}\"></i><h3>Security</h3><p>Stricter controls.</p></article><article><i class=\"{ic[3]}\"></i><h3>Design</h3><p>Accessible UI.</p></article></div>
	"""
		if feat == "steps":
			return f"""
	<ol class=\"feat steps\"><li><span>1</span> Prepare infrastructure</li><li><span>2</span> Roll out services</li><li><span>3</span> Validate quality</li><li><span>4</span> Open traffic</li></ol>
	"""
		# media
		return f"""
	<ul class=\"feat media\"><li><i class=\"{ic[0]}\"></i><div><h4>Observability</h4><p>Better traces & logs.</p></div></li><li><i class=\"{ic[1]}\"></i><div><h4>Scaling</h4><p>Autoscale tuning.</p></div></li><li><i class=\"{ic[2]}\"></i><div><h4>Security</h4><p>Least privilege.</p></div></li></ul>
	"""

	def art_html():
		if art == "orbs":
			return "<div class=\"art\"><div class=\"orb a\"></div><div class=\"orb b\"></div><div id=\"floaters\"></div></div>"
		if art == "waves":
			return "<svg class=\"bg waves\" viewBox=\"0 0 1440 320\"><path fill=\"currentColor\" fill-opacity=\"0.2\" d=\"M0,192L48,165.3C96,139,192,85,288,96C384,107,480,181,576,186.7C672,192,768,128,864,96C960,64,1056,64,1152,96C1248,128,1344,192,1392,224L1440,256L1440,0L0,0Z\"></path></svg>"
		if art == "stars":
			return "<canvas id=\"sky\"></canvas>"
		if art == "mesh":
			return "<div class=\"mesh\"></div>"
		if art == "blobs":
			return "<div class=\"blobs\"><span></span><span></span><span></span></div>"
		if art == "noise":
			return "<div class=\"noise\"></div>"
		if art == "stripes":
			return "<div class=\"stripes-bg\"></div>"
		return "<div class=\"triangles\"></div>"

	def footer_html():
		if foot == "simple":
			return "<footer class=\"footer simple\"><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>"
		if foot == "columns":
			return """
	<footer class=\"footer columns\"><div class=\"container\"><div><h4>Company</h4><a href=#>About</a><a href=#>Careers</a></div><div><h4>Product</h4><a href=#>Status</a><a href=#>Changelog</a></div><div><h4>Help</h4><a href=#>Docs</a><a href=#>Support</a></div></div></footer>
	"""
		if foot == "center":
			return "<footer class=\"footer center\"><div class=\"container\"><ul class=\"social\"><li><i class=\"fa fa-brands fa-x-twitter\"></i></li><li><i class=\"fa fa-brands fa-github\"></i></li><li><i class=\"fa fa-brands fa-discord\"></i></li></ul><small>© __YEAR__ __TITLE__</small></div></footer>"
		if foot == "social":
			return "<footer class=\"footer social\"><div class=\"container\"><a href=#><i class=\"fa fa-bell\"></i> Get updates</a><a href=#><i class=\"fa fa-envelope\"></i> Contact</a></div></footer>"
		return "<footer class=\"footer mini\"><div class=\"container\"><small>© __YEAR__ __TITLE__</small></div></footer>"

	# Hero composition
	hero_intro = f'<h1 class="title">{ctx["niche"]}<span class="tag">Maintenance</span></h1><p class="lead">{ctx["desc"]}</p>'
	hero_timer = timer_html()
	hero_art = art_html()
	if hero == "left":
		hero_html = f'<section class="hero left"><div class="copy">{hero_intro}{hero_timer}</div><div class="artbox">{hero_art}</div></section>'
	elif hero == "right":
		hero_html = f'<section class="hero right"><div class="artbox">{hero_art}</div><div class="copy">{hero_intro}{hero_timer}</div></section>'
	elif hero == "fullscreen":
		hero_html = f'<section class="hero fullscreen">{hero_art}<div class="center">{hero_intro}{hero_timer}</div></section>'
	else:
		hero_html = f'<section class="hero center"><div class="center">{hero_intro}{hero_timer}</div><div class="artbox">{hero_art}</div></section>'

	# Features and changelog
	features_block = features_html()
	changelog = """
	<section id=\"changelog\" class=\"changelog\"><div class=\"container\"><h2>Recent highlights</h2><div class=\"cards\"><article><h3>Infra</h3><p>Autoscaling & caching improvements.</p></article><article><h3>Security</h3><p>Rotated keys and hardened policies.</p></article><article><h3>UX</h3><p>Typography and motion polish.</p></article></div></div></section>
	"""

	# HTML doc
	html = f"""<!DOCTYPE html>
<html lang=\"en\"><head><meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<title>{ctx['title']} — Maintenance</title>
<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"/><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin/>
<link href=\"https://fonts.googleapis.com/css2?family={ctx['font_url']}&display=swap\" rel=\"stylesheet\"/>
<link rel=\"stylesheet\" href=\"{ctx['icon_url']}\"/>
<link rel=\"icon\" type=\"image/svg+xml\" href=\"favicon.svg\"/>
<link rel=\"stylesheet\" href=\"styles.css?v={ctx['code_hash']}\"/>
<script>window.MAINTENANCE_DEADLINE=\"{ctx['deadline_iso']}\";</script></head>
<body class=\"u-{uid}\">{nav_html()}<main>{hero_html}<section id=\"overview\" class=\"overview\"><div class=\"container\"><h2>What we're improving</h2>{features_block}</div></section>{changelog}<section id=\"status\" class=\"status\"><div class=\"container\"><h2>Timeline</h2><p>Targeting the countdown window. Subject to change for quality.</p></div></section><section id=\"contact\" class=\"contact\"><div class=\"container\"><a class=\"btn primary\" href=\"#\"><i class=\"fa fa-bell\"></i> Get alerts</a> <a class=\"btn ghost\" href=\"#\"><i class=\"fa fa-envelope\"></i> Support</a></div></section></main>{footer_html()}<script src=\"script.js?v={ctx['code_hash']}\"></script></body></html>"""

	# CSS per variant (condensed)
	css = ":root{--p:__P__;--s:__S__;--a:__A__;--bg:__B__;--gap:__G__px;--rad:__R__px}\n" \
		+ "*{box-sizing:border-box}html,body{height:100%}body{margin:0;font-family:'__FONT__',system-ui;color:#e6edf7;background:var(--bg)}\n" \
		+ ".container{max-width:1100px;margin:0 auto;padding:0 20px}\n" \
		+ ".btn{text-decoration:none;display:inline-flex;gap:10px;align-items:center;padding:10px 14px;border-radius:12px;border:1px solid rgba(255,255,255,.15)}\n" \
		+ ".btn.primary{background:var(--p);color:#0b0f1a;border-color:transparent}.btn.ghost{background:rgba(255,255,255,.06);color:#fff}\n" \
		+ "/* nav variants */\n" \
		+ f".nav-{uid}.top{{position:sticky;top:0;background:rgba(10,12,20,.6);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.08)}}\n" \
		+ f".nav-{uid}.top .container{{display:flex;justify-content:space-between;align-items:center;height:64px}}\n" \
		+ f".nav-{uid}.top .links{{display:none;gap:14px}}\n" \
		+ f".nav-{uid}.top .burger{{background:linear-gradient(90deg,var(--p),var(--s));border:0;color:#0b0f1a;padding:8px 12px;border-radius:10px}}\n" \
		+ f".nav-{uid}.top .menu{{display:none;position:absolute;right:20px;top:64px;background:#0b0f1a;border:1px solid rgba(255,255,255,.12);border-radius:12px;padding:12px;list-style:none;}}\n" \
		+ f".nav-{uid}.split .container{{display:flex;justify-content:space-between;align-items:center;height:64px}}\n" \
		+ f".nav-{uid}.split nav a{{margin:0 8px;color:#d8e7ff;text-decoration:none}}\n" \
		+ f".nav-{uid}.center .container{{display:grid;place-items:center;height:64px}}\n" \
		+ f".nav-{uid}.drawer .container{{display:flex;justify-content:space-between;align-items:center;height:64px}}\n" \
		+ f".nav-{uid}.drawer .drawer-panel{{display:none;position:absolute;left:20px;top:64px;background:#0b0f1a;border:1px solid rgba(255,255,255,.12);border-radius:12px;padding:12px}}\n" \
		+ f".nav-{uid}.sidebar{{position:fixed;top:0;left:0;bottom:0;width:220px;background:#0d1426;border-right:1px solid #1b2946;padding:14px}}\n" \
		+ ".bottombar{position:fixed;left:0;right:0;bottom:0;display:flex;gap:10px;justify-content:center;background:#0d1426;border-top:1px solid #1b2946;padding:10px}\n" \
		+ "\n/* hero */\n" \
		+ ".hero{display:grid;gap:24px;min-height:50vh;align-items:center}\n" \
		+ ".hero.left{grid-template-columns:1.1fr .9fr}.hero.right{grid-template-columns:.9fr 1.1fr}.hero.center{grid-template-columns:1fr;text-align:center}.hero.fullscreen{min-height:70vh;position:relative;overflow:hidden}\n" \
		+ f".title{{font-size:{44 + (salt%8)}px;line-height:1.1;margin:0 0 10px}}\n" \
		+ ".tag{display:inline-block;font-size:12px;margin-left:10px;padding:4px 10px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);color:var(--a)}\n" \
		+ ".lead{opacity:.92}\n" \
		+ ".art .orb{position:absolute;filter:blur(10px);opacity:.8}.art .a{width:220px;height:220px;border-radius:50%;background:radial-gradient(circle at 30% 30%,var(--s),transparent 60%);top:-20px;right:-10px;animation:float1 6s ease-in-out infinite}.art .b{width:180px;height:180px;border-radius:50%;background:radial-gradient(circle at 70% 70%,var(--a),transparent 60%);bottom:-10px;left:20px;animation:float2 7s ease-in-out infinite}\n" \
		+ ".bg.waves{position:fixed;left:0;right:0;bottom:0;z-index:-1;color:var(--s)}\n" \
		+ ".mesh{position:fixed;inset:0;background:radial-gradient(800px 400px at 10% 10%,rgba(124,58,237,.15),transparent),radial-gradient(800px 400px at 90% 90%,rgba(6,182,212,.15),transparent)}\n" \
		+ f".blobs span{{position:absolute;display:block;width:{60+salt%40}px;height:{60+salt%40}px;border-radius:50%;background:radial-gradient(circle at 30% 30%,var(--p),transparent)}}\n" \
		+ ".noise{position:fixed;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.03) 0 2px,transparent 2px 6px)}\n" \
		+ ".stripes-bg{position:fixed;inset:0;background:repeating-linear-gradient(90deg,rgba(99,102,241,.12) 0 2px,transparent 2px 40px)}\n" \
		+ ".triangles{position:fixed;inset:0;background:conic-gradient(from 0deg at 50% 50%,rgba(255,255,255,.04),transparent 20%)}\n" \
		+ "@keyframes float1{0%{transform:translateY(0)}50%{transform:translateY(-16px)}100%{transform:translateY(0)}}@keyframes float2{0%{transform:translateY(0)}50%{transform:translateY(-12px)}100%{transform:translateY(0)}}\n" \
		+ "\n/* features */\n" \
		+ ".overview .feat.list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(220px,1fr));gap:12px}\n" \
		+ ".overview .feat.cards{display:grid;grid-template-columns:repeat(4,minmax(180px,1fr));gap:12px}\n" \
		+ ".overview .feat.cards article{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:12px}\n" \
		+ ".overview .feat.steps{list-style:none;counter-reset:s;display:grid;gap:8px;padding:0;margin:0}\n" \
		+ ".overview .feat.steps li{display:grid;grid-template-columns:36px 1fr;gap:10px;align-items:center}\n" \
		+ ".overview .feat.steps li span{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--p);color:#0b0f1a;font-weight:700}\n" \
		+ ".overview .feat.media{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(2,minmax(220px,1fr));gap:12px}\n" \
		+ ".overview .feat.media li{display:flex;gap:12px;align-items:flex-start}\n" \
		+ "\n/* timer */\n" \
		+ ".timer.blocks{display:grid;grid-template-columns:repeat(4, minmax(80px,1fr));gap:12px;margin:16px 0}\n" \
		+ ".timer.blocks div{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);padding:12px;border-radius:12px;text-align:center}\n" \
		+ ".flipclock{display:grid;grid-template-columns:repeat(4,100px);gap:12px;margin:16px 0}\n" \
		+ ".fc{background:linear-gradient(180deg,#0d0d1e,#0b0b18);border:1px solid #20203a;border-radius:12px;padding:12px;text-align:center}\n" \
		+ ".fc span{display:block;font-weight:800;color:var(--s)}\n" \
		+ ".rings{position:relative;display:inline-grid;place-items:center;margin:10px 0}\n" \
		+ ".rings svg{transform:rotate(-90deg)}.rings .bg{fill:none;stroke:rgba(255,255,255,.1);stroke-width:8}\n" \
		+ ".ring{fill:none;stroke-width:8;stroke-linecap:round}.ring.d{stroke:var(--p)}.ring.h{stroke:var(--s)}.ring.m{stroke:var(--a)}.ring.s{stroke:#ffffff99}\n" \
		+ ".rings .labels{position:absolute;display:grid;grid-template-columns:repeat(4,auto);gap:8px;bottom:-30px}\n" \
		+ ".bars .bar{display:grid;grid-template-columns:80px 1fr 60px;gap:10px;align-items:center}\n" \
		+ ".bars .bar i{display:block;height:10px;border-radius:10px;background:linear-gradient(90deg,var(--p),var(--s))}\n" \
		+ ".chips span, .badges em{display:inline-block;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:8px 10px;margin-right:6px;color:var(--s)}\n" \
		+ ".digital{font-variant-numeric:tabular-nums;font-weight:800;letter-spacing:2px;color:var(--a)}\n" \
		+ ".stripes>div i{display:block;height:10px;border-radius:10px;background:linear-gradient(90deg,var(--p),var(--s));width:0}\n" \
		+ ".text-count strong{color:var(--s)}\n" \
		+ "\n/* sections */\n" \
		+ ".changelog .cards{display:grid;grid-template-columns:repeat(3,minmax(220px,1fr));gap:12px}\n" \
		+ ".changelog .cards article{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:12px}\n" \
		+ ".footer.center .social{list-style:none;display:flex;gap:10px;justify-content:center;margin:0 0 8px;padding:0}\n" \
		+ ".footer.columns .container{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}\n" \
		+ ".footer.social .container{display:flex;gap:12px;justify-content:center;padding:14px 0}\n" \
		+ "@media(max-width:860px){.hero.left,.hero.right{grid-template-columns:1fr}.changelog .cards{grid-template-columns:1fr}.overview .feat.cards{grid-template-columns:repeat(2,1fr)}.overview .feat.media{grid-template-columns:1fr}}\n"
	css = css.replace("__P__", ctx['colors']['primary']).replace("__S__", ctx['colors']['secondary']).replace("__A__", ctx['colors']['accent']).replace("__B__", ctx['colors']['bg']).replace("__G__", str(8+salt%8)).replace("__R__", str(10+salt%12)).replace("__FONT__", ctx['font_name'])

	# JS per timer variant
	js_parts = []
	js_parts.append("const q=s=>document.querySelector(s);")
	# nav interactions
	js_parts.append("{const b=q('.nav-"+uid+" .burger');const m=q('.nav-"+uid+" .menu');if(b&&m){b.addEventListener('click',()=>{const o=m.style.display==='block';m.style.display=o?'none':'block';b.setAttribute('aria-expanded',String(!o));});}}")
	js_parts.append("{const b=q('.nav-"+uid+" .drawer-btn');const d=q('#drawer');if(b&&d){b.addEventListener('click',()=>{const s=getComputedStyle(d).display!=='none';d.style.display=s?'none':'block';b.setAttribute('aria-expanded',String(!s));});}}")
	# stars background
	if art == "stars":
		js_parts.append("{const c=document.getElementById('sky');if(c){const x=c.getContext('2d');function R(){c.width=innerWidth;c.height=innerHeight}addEventListener('resize',R);R();const S=Array.from({length:160},()=>({x:Math.random()*c.width,y:Math.random()*c.height,z:Math.random()*2+.2}));function D(){x.clearRect(0,0,c.width,c.height);for(const s of S){x.fillStyle='rgba(255,255,255,'+(0.3+s.z/2)+')';x.fillRect(s.x,s.y,s.z,s.z);s.x+=0.05*s.z;if(s.x>c.width)s.x=0;}requestAnimationFrame(D)}D();}}")
	# countdown logic variants
	js_parts.append("const T=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);")
	js_parts.append("function Z(n){return n<10?'0'+n:String(n)}")
	if timer == "blocks" or timer == "chips" or timer == "digital":
		js_parts.append("function tick(){let ms=T-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);const d=q('#d'),h=q('#h'),m=q('#m'),s=q('#s');if(d)d.textContent=Z(D);if(h)h.textContent=Z(H);if(m)m.textContent=Z(M);if(s)s.textContent=Z(S);}setInterval(tick,1000);tick();")
	elif timer == "flip":
		js_parts.append("function set(el,v){if(!el)return;const p=el.textContent;el.textContent=v;if(p!==v){el.parentElement.classList.add('flip');setTimeout(()=>el.parentElement.classList.remove('flip'),600)}}function tick(){let ms=T-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);set(q('#fd'),Z(D));set(q('#fh'),Z(H));set(q('#fm'),Z(M));set(q('#fs'),Z(S));}setInterval(tick,1000);tick();")
	elif timer == "rings":
		js_parts.append("function SR(el,val,full){if(!el)return;const r=el.getAttribute('r');const L=2*Math.PI*r;el.setAttribute('stroke-dasharray',L);el.setAttribute('stroke-dashoffset',L*(1-val/full));}function tick(){let ms=T-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);SR(q('#cd'),D%365,365);SR(q('#ch'),H,24);SR(q('#cm'),M,60);SR(q('#cs'),S,60);const vd=q('#vd'),vh=q('#vh'),vm=q('#vm'),vs=q('#vs');if(vd)vd.textContent=Z(D);if(vh)vh.textContent=Z(H);if(vm)vm.textContent=Z(M);if(vs)vs.textContent=Z(S);}setInterval(tick,1000);tick();")
	elif timer == "bars":
		js_parts.append("function W(el,p){if(el)el.style.width=p+'%'}function tick(){let ms=T-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);W(q('#pd'),Math.min(100,(D%30)/30*100));W(q('#ph'),(H/24)*100);W(q('#pm'),(M/60)*100);W(q('#ps'),(S/60)*100);const vd=q('#vd'),vh=q('#vh'),vm=q('#vm'),vs=q('#vs');if(vd)vd.textContent=Z(D);if(vh)vh.textContent=Z(H);if(vm)vm.textContent=Z(M);if(vs)vs.textContent=Z(S);}setInterval(tick,1000);tick();")
	elif timer == "badges":
		js_parts.append("function tick(){let ms=T-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);const d=q('#d'),h=q('#h'),m=q('#m'),s=q('#s');if(d)d.textContent=D+'d';if(h)h.textContent=H+'h';if(m)m.textContent=M+'m';if(s)s.textContent=S+'s';}setInterval(tick,1000);tick();")
	elif timer == "stripes":
		js_parts.append("function S(el,p){if(el)el.style.width=p+'%'}function tick(){let ms=T-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);S(q('#sd'),Math.min(100,(D%30)/30*100));S(q('#sh'),(H/24)*100);S(q('#sm'),(M/60)*100);S(q('#ss'),(S/60)*100);}setInterval(tick,1000);tick();")
	else:
		js_parts.append("function tick(){let ms=T-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000),H=Math.floor(ms%86400000/3600000),M=Math.floor(ms%3600000/60000),S=Math.floor(ms%60000/1000);const td=q('#td'),th=q('#th'),tm=q('#tm'),ts=q('#ts');if(td)td.textContent=D;if(th)th.textContent=H;if(tm)tm.textContent=M;if(ts)ts.textContent=S;}setInterval(tick,1000);tick();")

	js = "(function(){" + "".join(js_parts) + "})();"

	# Enforce per-template unique class names by suffixing with -uid
	html = uniquify_html_classes(html, uid)
	css = uniquify_css_classes(css, uid)
	js = js.replace(".burger", f".burger-{uid}").replace(".menu'", f".menu-{uid}'").replace(".drawer-btn", f".drawer-btn-{uid}")

	return html, css, js


# Helpers to enforce per-template unique class names
# Suffix all custom classes with -<uid> while preserving third-party icon classes
CLASS_ICON_PREFIXES = ("fa", "bi", "bx")

def uniquify_html_classes(html: str, uid: str) -> str:
	def repl(m):
		classes = m.group(1)
		tokens = []
		for tok in classes.split():
			if tok.startswith(CLASS_ICON_PREFIXES) or tok.endswith(f"-{uid}"):
				tokens.append(tok)
			else:
				tokens.append(f"{tok}-{uid}")
		return 'class="' + ' '.join(tokens) + '"'
	return re.sub(r'class="([^"]+)"', repl, html)


def uniquify_css_classes(css: str, uid: str) -> str:
	# Append -uid to our authored class selectors when not yet suffixed
	roots = [
		'container','btn','primary','ghost','top','split','center','drawer','sidebar','bottom','links','burger','menu','drawer-btn','drawer-panel','bottombar',
		'hero','left','right','fullscreen','title','tag','lead','art','a','b','bg','waves','mesh','blobs','noise','stripes-bg','triangles','artbox',
		'overview','feat','list','cards','steps','media','changelog','status','contact','footer','simple','columns','social','mini','flipclock','fc','rings','bars','bar','chips','badges','digital','stripes','labels'
	]
	for r in roots:
		css = re.sub(fr'\.{re.escape(r)}(?!-[a-z0-9]{{1,8}})', f'.{r}-{uid}', css)
	# Also fix element combinations like .nav-<uid> .container to .nav-<uid> .container-<uid>
	css = re.sub(fr'(\s)\.container(\b)', fr'\1.container-{uid}\2', css)
	return css


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

		# Build theme-specific files for uniqueness
		ctx = {
			"title": niche,
			"niche": niche,
			"desc": desc,
			"features": features,
			"colors": palette,
			"font_url": font_url,
			"font_name": font_name,
			"icon_url": icon_url,
			"deadline_iso": deadline_iso,
			"code_hash": code_hash,
			"year": datetime.datetime.utcnow().year,
		}
		theme_keys = [
			"aurora","neon_grid","glass_rings","light_progress","terminal",
			"waves","stars","mosaic","sidebar_mesh","vaporwave"
		]
		# Distribute themes with some randomness to maximize uniqueness
		theme_key = theme_keys[(idx + random.randint(0, 7)) % len(theme_keys)]
		# Build unique composition per template for absolute uniqueness
		html_out, css_out, js_out = build_unique_template(ctx, salt=idx + random.randint(0, 99999))

		with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
			f.write(html_out)
		with open(os.path.join(folder, "styles.css"), "w", encoding="utf-8") as f:
			f.write(css_out)
		with open(os.path.join(folder, "script.js"), "w", encoding="utf-8") as f:
			f.write(js_out)
		with open(os.path.join(folder, "logo.svg"), "w", encoding="utf-8") as f:
			f.write(svg_logo_svg(palette['primary'], palette['secondary']))
		with open(os.path.join(folder, "favicon.svg"), "w", encoding="utf-8") as f:
			f.write(svg_favicon_svg(palette['primary'], palette['accent']))

		rel = os.path.relpath(os.path.join(folder, "index.html"), BASE_DIR)
		links.append((f"{niche} — unique-{idx}", rel))

	# Write connector and tutorial
	with open(CONNECTOR_PATH, "w", encoding="utf-8") as f:
		f.write(connector_html(links))
	with open(TUTORIAL_PATH, "w", encoding="utf-8") as f:
		f.write(tutorial_html())

	print(json.dumps({"generated": len(project_names), "output_dir": OUTPUT_DIR, "connector": CONNECTOR_PATH, "tutorial": TUTORIAL_PATH}))


if __name__ == "__main__":
	main()