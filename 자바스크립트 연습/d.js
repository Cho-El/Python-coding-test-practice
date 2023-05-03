function solution(originals, fakes) {
    let listOriginals = [];
    let listFakes = [];
    let answer = [];

    // original 값들을 전부 대문자로 바꾸고, 중복된 문자 제거 해서 List에 set형태로 넣기
    for (let i = 0; i < originals.length; i++) {
      // original 받아서 대문자로 바꾸기
      let origin = originals[i].toUpperCase();
      let setDict = new Set();
      // 해당 문자를 돌면서 setDict에 넣어주기
      for (let s of origin.split(" ")) {
        setDict.add(s);
      }
      // 위에서 만든 중복을 제거한 set형 딕셔너리를 List에 넣기
      listOriginals.push(setDict);
    }
    
    // 위와 똑같은 과정 fake에도 반복
    for (let i = 0; i < fakes.length; i++) {
      let fake = fakes[i].toUpperCase();
      let setDict = new Set();
      for (let s of fake.split(" ")) {
        setDict.add(s);
      }
      listFakes.push(setDict);
    }
    

    for (let fake of listFakes) {
      // fake 확인을 위한 문자
      let isFake = 0; // 표절이라면 1 표절이 아니라면 0
      for (let origin of listOriginals) {
        // 비교할 origin과 길이가 같은지 확인
        if (fake.size === origin.size) {
          isFake = 1;
          // 비교하는 fake를 돌면서 origin에 없는 내용이 하나라도 나온다면 표절이 아니므로 isFake를 0으로 초기화하고 break
          for (let s of fake) {
            if (!origin.has(s)) {
              isFake = 0;
              break;
            }
          }
          // 위에 문구가 다 돌았는데도 1이라면 표절임 그러므로 해당 origin은 비교 더 이상 할 필요 없으므로 break으로 포문 빠져나옴
          if (isFake) {
            break;
          }
        }
      }
      // answer에 값 집어넣기
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