function solution(s) {
  let answer = 0;
  let firstWord = s[0];
  let splitStr = s.split("");
  let correctCnt = 0;
  let test = "";

  for (let i = 0; i < splitStr.length; i++) {
    if (firstWord === splitStr[i]) {
      correctCnt += 1;
      test += splitStr[i];
    } else {
      if (correctCnt) {
        correctCnt -= 1;
        test += splitStr[i];

        if (correctCnt <= 0 && i !== splitStr.length - 1) {
          test += "|";
        }
      } else {
        if (test[test.length - 1] !== "|") {
          test += "|";
        }
        test += splitStr[i];
        firstWord = splitStr[i];
        correctCnt += 1;
      }
    }
  }

  /**
        첫 글자를 따서, 오른쪽으로 이동할 때마다 첫 글자와 같으면 카운트를 증가
        오른쪽으로 이동하면서 첫 글자와 같지 않으면 카운트를 증가하지 않음
    */
  return test.split("|").length;
}
