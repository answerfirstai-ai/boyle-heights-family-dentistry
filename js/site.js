(function(){
  // Hours [NEED: confirm] — Google listing: Mon–Thu 9–18, Sat 9–15, Fri/Sun closed
  var H={0:null,1:[9,18],2:[9,18],3:[9,18],4:[9,18],5:null,6:[9,15]};
  var la=new Date(new Date().toLocaleString("en-US",{timeZone:"America/Los_Angeles"}));
  var d=la.getDay(),h=la.getHours()+la.getMinutes()/60,t=H[d];
  document.querySelectorAll('.hours li[data-day="'+d+'"]').forEach(function(li){li.classList.add('today')});
  var open=t&&h>=t[0]&&h<t[1];
  function fmt(x){return (x>12?x-12:x)+(x>=12?' PM':' AM')}
  var msg='';
  if(open){msg='Open now · until '+fmt(t[1])}
  else{for(var k=0;k<8;k++){var dd=(d+k)%7,tt=H[dd];if(tt&&(k>0||h<tt[0])){msg='Closed now · opens '+(k===0?'today':k===1?'tomorrow':['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][dd])+' at '+fmt(tt[0]);break}}}
  document.querySelectorAll('.status').forEach(function(s){s.classList.toggle('open',!!open);s.querySelector('b').textContent=msg});
  // Callback form: no backend yet [NEED: form endpoint] — composes a text message to the office
  document.querySelectorAll('form.cb').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();
    if(!f.reportValidity())return;var n=f.elements.name.value.trim(),p=f.elements.phone.value.trim(),m=f.elements.message.value.trim();
    location.href='sms:+13232688308?&body='+encodeURIComponent('Callback request from '+n+' ('+p+')'+(m?': '+m:''));});});
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce||!window.gsap)return;
  var tiles=gsap.utils.toArray('.tiles .t');
  if(tiles.length){tiles.sort(function(a,b){return a.dataset.d-b.dataset.d});
    gsap.from(tiles,{scale:0,opacity:0,duration:.35,ease:'back.out(1.6)',stagger:{amount:1.2}});}
  if(window.ScrollTrigger){gsap.registerPlugin(ScrollTrigger);
    gsap.utils.toArray('.band').forEach(function(b){gsap.fromTo(b,{backgroundPositionX:'0px'},{backgroundPositionX:'144px',ease:'none',scrollTrigger:{trigger:b,start:'top bottom',end:'bottom top',scrub:true}})});
    gsap.utils.toArray('.arch').forEach(function(a){gsap.from(a,{clipPath:'inset(100% 0 0 0)',duration:.9,ease:'power3.out',scrollTrigger:{trigger:a,start:'top 85%'}})});}
})();
