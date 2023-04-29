function solution(originals, fakes) {
    let listOriginals = [];
    let listFakes = [];
    let answer = [];
    for (let i = 0; i < originals.length; i++) {
      let origin = originals[i].toUpperCase();
      let setDict = new Set();
      for (let s of origin.split(" ")) {
        setDict.add(s);
      }
      listOriginals.push(setDict);
    }
  
    for (let i = 0; i < fakes.length; i++) {
      let fake = fakes[i].toUpperCase();
      let setDict = new Set();
      for (let s of fake.split(" ")) {
        setDict.add(s);
      }
      listFakes.push(setDict);
    }
  
    for (let fake of listFakes) {
      let isFake = 0;
      for (let origin of listOriginals) {
        if (fake.size === origin.size) {
          isFake = 1;
          for (let s of fake) {
            if (!origin.has(s)) {
              isFake = 0;
              break;
            }
          }
          if (isFake) {
            break;
          }
        }
      }
      if (isFake) {
        answer.push(1);
      } else {
        answer.push(0);
      }
    }
  
    return answer;
}

console.log(solution(["A B C D E", "F G"], ["A b C d E", "E D C B A", "F G G G G", "A B C D E"]))
console.log(solution(["A A b C", "X Y Z", "A X Y"], ["A A b C X Y Z", "A B C X", "A C B C B", "Q", "A A b"]))