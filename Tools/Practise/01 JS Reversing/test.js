function intialDemo() {
    const step1 = 'console.log("yeet")';
    eval(step1)
    console.log({step1})
    console.log('------------------------------------')


    const step2 = `"${step1.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`
    console.log(step2);
    console.log(eval(step2));
    eval(eval(step2));
    console.log('------------------------------------')

    const step3 = `"${step2.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`
    console.log(step3);
    console.log(eval(step3));
    console.log(eval(eval(step3)));
    eval(eval(eval(step3)));
}

function loop() {
    let stepI = 'console.log("yeet2")'
    const n = 24

    for (let i = 0; i < n; i ++) {
        //console.log(stepI);
        stepI = `"${stepI.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`
    }

    console.log('------------------------------------')
    //console.log(stepI);
    console.log('------------------------------------')

    for (let i = 0; i < n; i ++) {
        stepI = eval(stepI);
        //console.log(stepI);
    }

    eval(stepI);
}

function notoobig() {
    function encrypt(str) {
        for (let i = 0; i < str.length; i ++) {
            if (str[i] === '*') {
                const start = str.substring(0, i);
                const end = str.substring(i+1);
                const num = parseInt(end);
                const end2 = str.substring(i+2+String(num).length)
                //console.log({start, end, num, end2})
                str = start + "*" + String(num+1) + "$" + end2;
            } else if (str[i] === '"') {
                str = str.substring(0, i) + "*1$" + str.substring(i+1);
            }
        }
        return str;
    }
    
    function decrypt(str) {
        for (let i = 0; i < str.length; i ++) {
            if (str[i] === '*') {
                const start = str.substring(0, i);
                const end = str.substring(i+1);
                const num = parseInt(end);
                const end2 = str.substring(i+2+String(num).length)
                //console.log({start, end, num, end2})
                if (num > 1) {
                    str = start + "*" + String(num-1) + "$" + end2;
                } else {
                    str = start + '"' + end2;
                }
            }
        }
        return str;
    }
    
    const n = 100000
    let jStr = 'console.log("yeet")'
    for (let j = 0; j < n; j ++) {
        //console.log(jStr);
        jStr = encrypt(jStr);
    }
    
    console.log(jStr);
    
    for (let j = 0; j < n; j ++) {
        jStr = decrypt(jStr);
        //console.log(jStr);
    }
    
    console.log(jStr)
}

function worksWithEval() {
    function encrypt(str) {
        for (let i = 0; i < str.length; i ++) {
            if (str[i] === '*') {
                const start = str.substring(0, i);
                const end = str.substring(i+1);
                const num = parseInt(end);
                const end2 = str.substring(i+2+String(num).length)
                //console.log({start, end, num, end2})
                str = start + "*" + String(num+1) + "$" + end2;
            } else if (str[i] === '"') {
                str = str.substring(0, i) + "*1$" + str.substring(i+1);
            }
        }
        return str;
    }
    
    function decrypt(str) {
        for (let i = 0; i < str.length; i ++) {
            if (str[i] === '*') {
                const start = str.substring(0, i);
                const end = str.substring(i+1);
                const num = parseInt(end);
                const end2 = str.substring(i+2+String(num).length)
                //console.log({start, end, num, end2})
                if (num > 1) {
                    str = start + "*" + String(num-1) + "$" + end2;
                } else {
                    str = start + '"' + end2;
                }
            }
        }
        return str;
    }
    
    
    /*const step1 = 'console.log("yeet"); 7331'
    const step2 = `console.log("yeet2"); decrypt("${encrypt(step1)}")`
    console.log({step2});
    const test2 = eval(step2)
    console.log({test2})
    const test1 = eval(test2);
    console.log({test1})*/
    
    const n = 500;
    let jStr = 'console.log("yeet"); 7331'
    for (let j = 0; j < n; j ++) {
        jStr = `console.log("yeeet${j+1}"); decrypt("${encrypt(jStr)}")`
    }
    console.log({jStr})
    
    for (let j = 0; j < n + 1; j ++) {
        jStr = eval(jStr);
    }
    
    console.log(jStr);
}

function ceasar() {
    const alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

function encrypt(str) {
    for (let i = 0; i < str.length; i ++) {
        if (str[i] === '*') {
            const start = str.substring(0, i);
            const end = str.substring(i+1);
            const num = parseInt(end);
            const end2 = str.substring(i+2+String(num).length)
            //console.log({start, end, num, end2})
            str = start + "*" + String(num+1) + "$" + end2;
        } else if (str[i] === '"') {
            str = str.substring(0, i) + "*1$" + str.substring(i+1);
        } else if (alphabet.includes(str[i])) {
            str = str.substring(0, i) + alphabet[alphabet.indexOf(str[i]) + 1] + str.substring(i+1);
        }
    }
    return str;
}

function decrypt(str) {
    for (let i = 0; i < str.length; i ++) {
        if (str[i] === '*') {
            const start = str.substring(0, i);
            const end = str.substring(i+1);
            const num = parseInt(end);
            const end2 = str.substring(i+2+String(num).length)
            //console.log({start, end, num, end2})
            if (num > 1) {
                str = start + "*" + String(num-1) + "$" + end2;
            } else {
                str = start + '"' + end2;
            }
        } else if (alphabet.includes(str[i])) {
            str = str.substring(0, i) + alphabet[alphabet.lastIndexOf(str[i]) - 1] + str.substring(i+1);
        }
    }
    return str;
}


/*const step1 = 'console.log("yeet"); 7331'
const step2 = `console.log("yeet2"); decrypt("${encrypt(step1)}")`
console.log({step2});
const test2 = eval(step2)
console.log({test2})
const test1 = eval(test2);
console.log({test1})*/

const n = 100;
let jStr = 'console.log("yeet"); 7331'
for (let j = 0; j < n; j ++) {
    jStr = `console.log("yeeet${j+1}"); decrypt("${encrypt(jStr)}")`
}
console.log({jStr})

for (let j = 0; j < n + 1; j ++) {
    jStr = eval(jStr);
}

console.log(jStr);
}

const alphabet = " ={}():;abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ={}():;abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

function encrypt(str) {
    for (let i = 0; i < str.length; i ++) {
        if (str[i] === '#') {
            const start = str.substring(0, i);
            const end = str.substring(i+1);
            const num = parseInt(end);
            const end2 = str.substring(i+2+String(num).length)
            //console.log({start, end, num, end2})
            str = start + "#" + String(num+1) + "$" + end2;
        } else if (str[i] === '"') {
            str = str.substring(0, i) + "#1$" + str.substring(i+1);
        } else if (alphabet.includes(str[i])) {
            str = str.substring(0, i) + alphabet[alphabet.indexOf(str[i]) + 1] + str.substring(i+1);
        }
    }
    return str;
}

function decrypt(str) {
    for (let i = 0; i < str.length; i ++) {
        if (str[i] === '#') {
            const start = str.substring(0, i);
            const end = str.substring(i+1);
            const num = parseInt(end);
            const end2 = str.substring(i+2+String(num).length)
            //console.log({start, end, num, end2})
            if (num > 1) {
                str = start + "#" + String(num-1) + "$" + end2;
            } else {
                str = start + '"' + end2;
            }
        } else if (alphabet.includes(str[i])) {
            str = str.substring(0, i) + alphabet[alphabet.lastIndexOf(str[i]) - 1] + str.substring(i+1);
        }
    }
    return str;
}


/*const step1 = 'console.log("yeet"); 7331'
const step2 = `console.log("yeet2"); decrypt("${encrypt(step1)}")`
console.log({step2});
const test2 = eval(step2)
console.log({test2})
const test1 = eval(test2);
console.log({test1})*/

function step(str) { return `d("${encrypt(str)}")` }

let jStr = 'console.log("Yeeeeet")'

for (let j = 0; j < 102; j ++) {
    jStr = `debugger;${step(jStr)}`
}

for (let j = 0; j < 32; j ++) {
    jStr = `if ("jdkashfjhakefjajknjksdna" === "asfeaeawt4awaw4tawgar"){"asdfgaew"};${step(jStr)}`
}
jStr = `if (document.getElementById("pass").value === "theinception"){alert("goood job!");};${step(jStr)}`
for (let j = 0; j < 47; j ++) {
    jStr = `if ("jdkashfjhakefjajknjksdna" === "asfeaeawt4awaw4tawgar"){"asdfgaew"};${step(jStr)}`
}


for (let j = 0; j < 31; j ++) {
    const random = Math.random * 1000;
    jStr = `${random}; ${step(jStr)}`
}

jStr = `start === Math.round(Date.now()/5000) ? ${step(jStr)} : ""`

for (let j = 0; j < 37; j ++) {
    jStr = `debugger;${step(jStr)}`
}

jStr = `var start = Math.round(Date.now()/5000); ${step(jStr)}`

for (let j = 0; j < 176; j ++) {
    jStr = `debugger;${step(jStr)}`
}

/*for (let j = 0; j < n + 1; j ++) {
    jStr = eval(jStr);
}*/

console.log(`var data = '${jStr}'`)
