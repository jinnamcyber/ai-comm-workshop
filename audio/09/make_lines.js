// node audio/09/make_lines.js  -> lines.json (列舉所有替換詞組合)
const fs=require('fs'),path=require('path');
const html=fs.readFileSync(path.join(__dirname,'../../09-葡文情境對話.html'),'utf8');
let code=html.match(/<script>([\s\S]*?)<\/script>/)[1].replace('/*ENUM*/','global.__X={SCS,numPt,sc:()=>SCS};');
const mk=()=>({innerHTML:'',textContent:'',hidden:false,classList:{add(){},remove(){}},setAttribute(){},getAttribute(){return null},style:{}});
global.document={querySelector:()=>mk(),addEventListener(){},documentElement:{}};
global.window=global;global.requestAnimationFrame=f=>f();
eval(code);
const {SCS}=global.__X;
// 角色→聲線：每場景 A/B
const F='pt-PT-RaquelNeural',M='pt-PT-DuarteNeural';
const V=[{A:F,B:M},{A:F,B:M},{A:M,B:F}];
const out=new Map();const add=(text,voice)=>{const k=text.replace(/\s+/g,'')+'|'+voice;if(!out.has(k))out.set(k,{text,voice});};
SCS.forEach((s,si)=>{
  const keys=Object.keys(s.slotN);let combos=[{}];
  keys.forEach(k=>{const n=[];combos.forEach(c=>{for(let i=0;i<s.slotN[k];i++)n.push({...c,[k]:i});});combos=n;});
  combos.forEach(t=>{
    s.lines.forEach(L=>add(L.pt.replace(/\{(\w+)\}/g,(m,k)=>s.tok(k,t).pt),V[si][L.r]));
    s.quiz(t).forEach(q=>add(q.pt,F));
  });
});
const arr=[...out.values()];
fs.writeFileSync(path.join(__dirname,'lines.json'),JSON.stringify(arr,null,1));
console.log(arr.length);
