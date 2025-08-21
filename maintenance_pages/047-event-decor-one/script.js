(function(){function q(s){return document.querySelector(s)};const target=new Date(window.MAINTENANCE_DEADLINE||Date.now()+86400000);
function fmt(){let ms=target-new Date();if(ms<0)ms=0;const D=Math.floor(ms/86400000);const H=Math.floor(ms%86400000/3600000);const M=Math.floor(ms%3600000/60000);const S=Math.floor(ms%60000/1000);
return D+'d '+H+'h '+M+'m '+S+'s';}
setInterval(()=>{const pre=q('pre');if(pre){pre.innerHTML=pre.innerHTML.replace(/\$ __COUNTDOWN__.*/,'$ __COUNTDOWN__ '+fmt())}},1000);})();