const fs=require('fs');
const h=fs.readFileSync(__dirname+'/../../08-閱讀口語對答.html','utf8');
function grab(name){const m=h.match(new RegExp('var '+name+'=(\\[[\\s\\S]*?\\n\\]);'));return eval(m[1]);}
const STORY=grab('STORY'),QS=grab('QS');
const HIU='zh-HK-HiuMaanNeural',WAN='zh-HK-WanLungNeural';
const out=[],seen={};
function add(t,v){const k=t.replace(/\s+/g,'')+v;if(seen[k])return;seen[k]=1;out.push({text:t,voice:v});}
STORY.forEach(p=>p.forEach(s=>add(s,HIU)));
QS.forEach((q,i)=>{
  add('第'+(i+1)+'題。',WAN);add(q.q,WAN);add(q.hint,WAN);add(q.ans,WAN);
});
['好叻呀！一次就答啱！','你好叻喎！試多一次就答啱喇！','講得好呀，多謝你同我分享！','我嘅例子係：','完整答案係：','可以再講多少少嗎？','差少少喔，唔緊要，再試吓！','冇問題，我哋一齊睇吓答案：','全部答啱，好叻呀！'].forEach(t=>add(t,WAN));
for(let n=0;n<=5;n++)add('完成啦！你答啱咗5題入面嘅'+n+'題。',WAN);
const N=['第一段','第二段','第三段','第四段'];
for(let m=1;m<16;m++){const a=N.filter((_,i)=>m&(1<<i));add('可以溫習'+a.join('同')+'。',WAN);}
fs.writeFileSync(__dirname+'/lines.json',JSON.stringify(out,null,1));
console.log(out.length);
