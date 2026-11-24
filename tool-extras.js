/* 共用：右下角「複製 Prompt」按鈕（SVG 圖示，無 emoji）。需要 prompts.js */
(function(){
  var slug; try{ slug = decodeURIComponent(location.pathname.split('/').pop()).replace(/\.html$/,''); }catch(e){ return; }
  var P = (window.TOOL_PROMPTS||{})[slug]; if(!P || !P.good) return;
  var css = document.createElement('style');
  css.textContent = '.cpBtn{position:fixed;right:16px;bottom:16px;z-index:9990;display:flex;align-items:center;gap:8px;min-height:56px;padding:0 20px;border:3px solid #1F2A44;border-radius:999px;background:#fff;color:#1F2A44;font:700 18px/1 system-ui,"PingFang HK","Noto Sans TC",sans-serif;box-shadow:0 5px 0 #1F2A44;cursor:pointer}'+
  '.cpBtn:active{transform:translateY(3px);box-shadow:0 2px 0 #1F2A44}.cpBtn svg{width:24px;height:24px}'+
  '.cpOv{position:fixed;inset:0;z-index:9991;background:rgba(20,28,50,.55);display:flex;align-items:center;justify-content:center;padding:16px}.cpOv[hidden]{display:none}'+
  '.cpBox{background:#fff;color:#1F2A44;border-radius:24px;width:min(860px,100%);max-height:92vh;display:flex;flex-direction:column;padding:20px 22px;gap:12px;font-family:system-ui,"PingFang HK","Noto Sans TC",sans-serif}'+
  '.cpBox h2{margin:0;font-size:22px}.cpBox p{margin:0;color:#5B6478;font-size:16px}'+
  '.cpTxt{flex:1;min-height:120px;overflow:auto;white-space:pre-wrap;background:#F6F3EA;border:2px solid #E5DECB;border-radius:16px;padding:14px 16px;font-size:16px;line-height:1.65;user-select:all}'+
  '.cpRow{display:flex;gap:10px;justify-content:flex-end;flex-wrap:wrap}.cpRow button{min-height:56px;padding:0 24px;border-radius:16px;border:3px solid #1F2A44;font:700 18px system-ui,"PingFang HK",sans-serif;cursor:pointer;background:#fff;color:#1F2A44}.cpRow .go{background:#2E8B4F;border-color:#1F2A44;color:#fff}'+
  '@media print{.cpBtn,.cpOv{display:none!important}}';
  document.head.appendChild(css);
  var ICON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="8" width="12" height="12" rx="2.5"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"/></svg>';
  var b=document.createElement('button'); b.type='button'; b.className='cpBtn'; b.innerHTML=ICON+'<span>複製 Prompt</span>';
  var ov=document.createElement('div'); ov.className='cpOv'; ov.hidden=true;
  ov.innerHTML='<div class="cpBox" role="dialog" aria-label="複製 Prompt"><h2></h2><p>呢段就係用嚟做出呢個教具嘅 Prompt，複製後貼入 Gemini（Canvas）就得。</p><div class="cpTxt" id="cpTxt"></div><div class="cpRow"><button type="button" id="cpClose">關閉</button><button type="button" class="go" id="cpCopy">複製全部</button></div></div>';
  function mount(){ document.body.appendChild(b); document.body.appendChild(ov);
    ov.querySelector('h2').textContent=(P.title||slug);
    ov.querySelector('#cpTxt').textContent=P.good.replace(/\*\*/g,'');
    b.onclick=function(){ ov.hidden=false; };
    ov.querySelector('#cpClose').onclick=function(){ ov.hidden=true; };
    ov.onclick=function(e){ if(e.target===ov) ov.hidden=true; };
    document.addEventListener('keydown',function(e){ if(e.key==='Escape') ov.hidden=true; });
    ov.querySelector('#cpCopy').onclick=function(){
      var t=P.good.replace(/\*\*/g,''), btn=this;
      function ok(){ btn.textContent='已複製'; setTimeout(function(){ btn.textContent='複製全部'; },1800); }
      function fb(){ var r=document.createRange(); r.selectNodeContents(ov.querySelector('#cpTxt')); var s=getSelection(); s.removeAllRanges(); s.addRange(r); try{ document.execCommand('copy'); ok(); }catch(e){ btn.textContent='請手動複製'; } }
      if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(t).then(ok,fb); } else fb();
    };
  }
  if(document.body) mount(); else document.addEventListener('DOMContentLoaded',mount);
})();
