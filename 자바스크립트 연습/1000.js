const fs = require('fs');
const inputData = fs.readFileSync(__dirname + "/example.txt").toString().split(' ');

const input = ['472','385','111'].map(parseInt)

let a = [1,2,3,4].map((a,b,c,d) => a + b)

let test = [1,2]
test.push(10)
console.log(test) // [1,2,10]
let popElement = test.pop()
console.log(popElement) // 10
console.log(test) // [1,2]

test = [2,3,4,5]
console.log(test.join('\n'))

let test2 = 'a b c d'
let test3 = test2.replace('a','h')

console.log(test3)
let newArray = test2.split()
console.log(newArray)

console.log('\\    /\\')
console.log(' )  ( \')')
console.log('(  /  )')
console.log(' \\(__)|')


var array1 = ['1','2','3']
var changeArray = array1.map((x) => Number(x))
console.log(changeArray)

console.log(false)

let str1 = "a"
let int1 = 1
console.log(`str1 : ${str1}, int1 : ${int1}`)

let array = new Array()
let N = 10
for (let i = 0; i < N; i++) {
    array[i] = i + 1
}