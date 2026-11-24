/* 唔用電腦內置（機械）朗讀：預錄 mp3 冇覆蓋嘅句子就靜音，但照常觸發 onstart/onend，令動畫同流程唔會卡住。
   冇預錄嘅句子會記喺 window.__NO_VOICE（同 console），方便補錄。 */
(function(){
  try{
    var s = window.speechSynthesis; if(!s) return;
    window.__NO_VOICE = window.__NO_VOICE || [];
    s.speak = function(u){
      try{
        var t = (u && u.text) || '';
        window.__NO_VOICE.push(t);
        try{ console.info('[no-voice]', t); }catch(e){}
        if(u && u.onstart){ try{ u.onstart({}); }catch(e){} }
        var ms = Math.min(6000, Math.max(900, t.length * 170));
        if(u && (u.onend || u.onerror)) setTimeout(function(){ try{ (u.onend || u.onerror)({}); }catch(e){} }, ms);
      }catch(e){}
    };
    s.getVoices = function(){ return []; };
  }catch(e){}
})();
