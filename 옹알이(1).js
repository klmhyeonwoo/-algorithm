function solution(babbling) {
    const canSpeak = ['aya', 'ye', 'woo', 'ma'];
    let answer = 0;
    
    for (let j=0; j<babbling.length; j++) {
        for (let i=0; i<babbling.length; i++)
        {
            canSpeak.map((item) => {
                if (babbling[j].includes(item)) {
                    if (babbling[j].indexOf(item) === 0) {
                        babbling[j] = babbling[j].replace(item, '');
                        if (babbling[j] == "") {
                            answer += 1;
                        }
                    }
                } 
            });
        }
    }

    return answer;
}