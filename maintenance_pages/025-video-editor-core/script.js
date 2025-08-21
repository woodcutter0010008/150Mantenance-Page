(function(){
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
