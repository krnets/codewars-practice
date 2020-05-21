// 6kyu - Most consecutive 0's in a row [Code-golf]

f=inp=>(''+inp).match(/(0)+/g).sort().slice(-1)[0].length
// f=inp=>(''+inp).match(/0{1,}/g).sort().pop().length
// f=inp=>(inp+'').split(/[1-9]/).sort().reverse()[0].length
// f=y=>Math.max(...(''+y).match(/(0+)/g).map(x=>x.length))
// f=s=>Math.max(...(s+'').match(/0+/g).map(el=>el.length))
// f=n=>Math.max(...(n+'').match(/(0+)/g).map(i=>i.length))
// f=n=>Math.max(...(""+n).match(/0*/g).map(s=>s.length))
// f=n=>Math.log10(Math.max(...(n+"").match(/\d0+/g)))|0
// f=(i,n=1)=>`${i}`.indexOf('0'.repeat(n))<0?n-1:f(i,n+1)
// f=i=>(''+i).split(/[1-9]/).sort().reverse()[0].length
// f=i=>`${i}`.match(/0+/g).sort().slice(-1)[0].length
// f=n=>(''+n).match(/0+/g).sort((a,b)=>a<b)[0].length
// f=inp=>`${inp}`.match(/0+/g).sort().pop().length
// f=_=>`${_}`.match(/0+/g).sort``.pop``.length
// f=i=>`${i}`.match(/0+/g).sort``.pop``.length
// f=Q=>/(0+)(?!.*\1)/.exec(Q)[1].length


q = f(1002000) // 3
q
q = f(10002030000) // 4
q
q = f(10) // 1
q