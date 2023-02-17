const obj = { name: "hyeon woo" };

function say(job, skill) {
    console.log(`Hello, my name is ${this.name}, my job is ${job}, my tech skill is ${skill}`);
};

say.call(obj, "front-end developer", "react");
say.apply(obj, ["back-end developer", "springBoot"]);
const bound = say.bind(obj, "designer", "figma");
bound();