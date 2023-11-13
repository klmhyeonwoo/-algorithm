function solution(s) {
  let leftBracket = 0;
  let rightBracket = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] == "(") {
      leftBracket += 1;
    }
    if (leftBracket > rightBracket) {
      if (s[i] == ")") {
        rightBracket += 1;
      }
    } else {
      return false;
    }
  }

  if (rightBracket === leftBracket) {
    return true;
  } else {
    return false;
  }
}
