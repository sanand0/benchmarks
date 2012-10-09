var data = [];
for (var i=0; i<50000000; i++) { data[i] = i; }

t0 = new Date();
for (var i=0; i<50000000; i++) { data[i] = data[i] + 1; }
t1 = new Date();

console.log(t1 - t0, 'ms');
