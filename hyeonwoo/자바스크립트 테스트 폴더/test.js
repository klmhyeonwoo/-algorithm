function obj() {
	this.a = 10;
    this.b = 20;
}

obj.prototype.sum = () => {
	return this.a + this.b;
}

obj.prototype.sum2 = function() {
    return this.a + this.b;
}

var firstObj = new obj();

console.log(firstObj.a);
console.log(firstObj.b);
console.log(firstObj.sum());
console.log(firstObj.sum2());