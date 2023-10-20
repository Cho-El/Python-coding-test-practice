const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
 
let input = [];
let count = 0;
rl.on('line', function (line) {
    count++;
    if(count <= 2) {
        input.push(Number(line));
    }else {
        rl.close();
    }
});
 
rl.on('close', function () {
    let A = input[0];
    let B = input[1];
    
    let firstNum = B % 10;
    let secondNum = (B % 100 - B % 10) / 10;
    let thirdNum = (B - B % 100) / 100;
 
    let result1 = firstNum * A;
    let result2 = secondNum * A;
    let result3 = thirdNum * A;
 
    let result4 = result3 * 100 + result2 * 10 + result1;
    
    console.log(result1);
    console.log(result2);
    console.log(result3);
    console.log(result4);
});