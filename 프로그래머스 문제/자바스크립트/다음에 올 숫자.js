// 첫번째 풀이
function solution1(common) {
    let result = 0
    let judgeMent = 0
    // 등차인지 등비인지 판단
    if (common[1] - common[0] === common[2] - common[1]) {
        // 등차
        judgeMent = 1
    } else {
        // 등비
        judgeMent = 0
    }

    if (judgeMent) {
        // 등차 마지막값 반환
        let dist = common[1] - common[0]
        result = common[common.length - 1] + dist
    } else {
        // 등비 마지막값 반환
        let dist = common[1] / common[0]
        result = common[common.length - 1] * dist
    }

    return result;
}

// 두번째 풀이
function solution(common) {
    let result = 0
    // 등차인지 등비인지 판단
    if (common[1] - common[0] === common[2] - common[1]) {
        // 등차
        return common[common.length - 1] + common[1] - common[0]
    } else {
        // 등비
        return common[common.length - 1] * common[1] / common[0]
    }
}

let input = new Array(1,2,3,4)
console.log(solution(input))
input = [2, 4, 8]
console.log(solution(input))