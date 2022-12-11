function solution(id_pw, db) {
    let ID_CHECK = false;
    let PW_CHECK = false;

    db.map((item) => {

        console.log(item, id_pw)
        if (item[0] === id_pw[0]) {
            ID_CHECK = true;
        }

        if (ID_CHECK && item[1] === id_pw[1]) {
            PW_CHECK = true;
        }
    })

    if (ID_CHECK && PW_CHECK) {
        return "login";
    } else if (ID_CHECK && PW_CHECK === false) {
        return "wrong pw";
    } else {
        return "fail";
    }
}

console.log(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]));