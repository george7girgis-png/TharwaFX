// An isolated simulation. No network or order execution endpoints.
(function () {
  const root = document.querySelector('[data-terminal]');
  if (!root) return;
  const get = selector => root.querySelector(selector), chart = get('[data-chart]');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const specs = {XAUUSD:[2398.28,1.8,.07,2],EURUSD:[1.16698,.0005,.00006,5],BTCUSD:[68441.5,85,29.5,1]};
  let symbol='XAUUSD', frame='H1', paused=reduced, candles=[], last, seed=41;
  const random = () => ((seed=seed*16807%2147483647)/2147483647);
  const number = n => n.toLocaleString('en-US',{minimumFractionDigits:specs[symbol][3],maximumFractionDigits:specs[symbol][3]});
  function node(tag, attrs, text, parent=chart) {
    const e=document.createElementNS('http://www.w3.org/2000/svg',tag);
    Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));
    if(text!==undefined)e.textContent=text;
    parent.appendChild(e); return e;
  }
  function next() {
    const step=specs[symbol][1]*({M1:.4,M15:.7,H1:1,H4:1.7}[frame]);
    const open=last,close=open+(random()-.5)*step*2;
    candles.push({open,close,high:Math.max(open,close)+random()*step*.6,low:Math.min(open,close)-random()*step*.6});
    if(candles.length>62)candles.shift();last=close;
  }
  function draw(animate=false) {
    chart.replaceChildren();
    let lo=Math.min(...candles.map(c=>c.low)),hi=Math.max(...candles.map(c=>c.high));
    const pad=(hi-lo)*.18;lo-=pad;hi+=pad;
    const y=v=>20+(hi-v)/(hi-lo)*320;
    for(let row=0;row<5;row++) {
      const yy=20+row*80;
      node('line',{x1:0,x2:785,y1:yy,y2:yy,stroke:'#25382b','stroke-dasharray':'3 6'});
      node('text',{x:800,y:yy+4,fill:'#77917f','font-size':11,'font-family':'monospace'},number(hi-row*(hi-lo)/4));
    }
    for(let col=0;col<7;col++) {
      node('line',{x1:col*128,x2:col*128,y1:20,y2:345,stroke:'#1b2b21'});
      node('text',{x:col*128,y:375,fill:'#77917f','font-size':11,'font-family':'monospace'},String(9+col).padStart(2,'0')+':00');
    }
    candles.forEach((c,i)=>{
      const x=8+i*12.35,color=c.close>=c.open?'#63e982':'#ef8174';
      const g=node('g',i===61&&animate?{class:'terminal-candle'}:{});
      node('line',{x1:x+3,x2:x+3,y1:y(c.high),y2:y(c.low),stroke:color,'stroke-width':1.3},undefined,g);
      node('rect',{x,y:y(Math.max(c.open,c.close)),width:6,height:Math.max(2,Math.abs(y(c.open)-y(c.close))),fill:color,rx:1},undefined,g);
    });
    node('line',{x1:0,x2:785,y1:y(last),y2:y(last),stroke:'#75eba0','stroke-dasharray':'5 5',opacity:.6});
    node('circle',{cx:8+61*12.35+3,cy:y(last),r:4,fill:'#adffc1'});
    chart.setAttribute('aria-label',`Simulated ${symbol} candlestick chart, ${frame} timeframe`);
    get('[data-price]').textContent=number(last);
    get('[data-bid]').textContent=number(last-specs[symbol][2]);
    get('[data-ask]').textContent=number(last);
    get('[data-instrument]').textContent=symbol+' / '+frame;
  }
  function reset(){candles=[];seed=41+Object.keys(specs).indexOf(symbol)*17;last=specs[symbol][0];for(let i=0;i<62;i++)next();draw();}
  function buttons(selector,update){root.querySelectorAll(selector).forEach(b=>b.addEventListener('click',()=>{root.querySelectorAll(selector).forEach(other=>other.setAttribute('aria-pressed',String(other===b)));update(b);reset();}));}
  buttons('[data-symbol]',b=>symbol=b.dataset.symbol);
  buttons('[data-frame]',b=>frame=b.dataset.frame);
  const pause=get('[data-pause]');
  function motion(){pause.setAttribute('aria-pressed',String(paused));pause.textContent=paused?'Resume animation':'Pause animation';get('[data-motion-label]').textContent=paused?'Animation paused':'Animated preview';root.classList.toggle('is-paused',paused);}
  pause.addEventListener('click',()=>{paused=!paused;motion();});
  const volume=get('#preview-volume');
  function lots(){const n=Number(volume.value);return Number.isFinite(n)?Math.min(100,Math.max(.01,n)):.1;}
  root.querySelectorAll('[data-volume-step]').forEach(b=>b.addEventListener('click',()=>volume.value=Math.min(100,Math.max(.01,lots()+Number(b.dataset.volumeStep))).toFixed(2)));
  volume.addEventListener('change',()=>volume.value=lots().toFixed(2));
  root.querySelectorAll('[data-preview-side]').forEach(b=>b.addEventListener('click',()=>{const side=b.dataset.previewSide;get('[data-feedback]').textContent=`Preview: ${side} ${lots().toFixed(2)} lots of ${symbol} at ${number(side==='Buy'?last:last-specs[symbol][2])}. No order has been placed.`;}));
  reset();motion();
  setInterval(()=>{if(paused||document.hidden)return;const r=root.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;next();draw(!reduced);},1800 / (window.TFX_MOTION_RATE || 0.8));
})();
