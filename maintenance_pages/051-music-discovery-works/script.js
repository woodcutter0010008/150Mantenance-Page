(function(){function q(s){return document.querySelector(s)};function w(el,val){if(!el)return;el.style.width=val+'%'};function t(el,txt){if(el)el.textContent=txt}
const pd=q('#pd'),ph=q('#ph'),pm=q('#pm'),ps=q('#ps');const vd=q('#vd'),vh=q('#vh'),vm=q('#vm'),vs=q('#vs');
const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);function pad(n){return n<10?'0'+n:String(n)}
function tick(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000);const H=Math.floor(ms%86400000/3600000);const M=Math.floor(ms%3600000/60000);const S=Math.floor(ms%60000/1000);
const pH=(H/24)*100,pM=(M/60)*100,pS=(S/60)*100;w(pd,Math.min(100,(D%30)/30*100));w(ph,pH);w(pm,pM);w(ps,pS);t(vd,pad(D));t(vh,pad(H));t(vm,pad(M));t(vs,pad(S));}
setInterval(tick,1000);tick();})();