function order(food) {
    console.log(`${food}을(를) 주문하셨습니다.`);

    return function (drink) {
        console.log(`${drink}을(를) 추가로 주문하셨습니다.`);
    }
}


const orderBurger = order("햄버거");
const orderPizza = order("피자");
orderBurger("콜라");
orderPizza("사이다");