let x = 1;

// 상위 스코프를 결정하는 방식은, 자신이 어디서 호출되었는지가 아닌 어디서 정의되었는지를 확인한다.

function foo() {
    var x = 10;
    bar ();
};

function bar() {
    console.log(x);
};

foo(); // bar에서 x를 찾으려고 하는데, 외부에 없으니까 상위스코프인 전역 x 변수를 가져옴
bar(); // bar에서 x를 찾으려고 하는데, 외부에 없으니까 상위스코프인 전역 x 변수를 가져옴