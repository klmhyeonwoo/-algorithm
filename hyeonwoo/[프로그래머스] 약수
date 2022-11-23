function solution(dots) {
    const store = [];
    for (let i=0; i<dots.length; i++)
    {
        for (let k=i+1; k<dots.length; k++)
        {
            // y좌표의 차이 / x좌표의 차이 = 기울기
            const dataOfNum = (dots[i][1] - dots[k][1]) / (dots[i][0] - dots[k][0]);
            if (store.includes(dataOfNum))
            {
                return 1;
            }
            store.push(dataOfNum);
        }
    }
    return 0;
}
