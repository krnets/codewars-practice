// function promiseHelloWorld() {
//     return new Promise((resolve, reject) => setTimeout(function () {
//         resolve('Hello World!')
//     }, 1000))
// }

// async function promiseHelloWorld() {
//     return 'Hello World!';
// }

// const promiseHelloWorld = () => Promise.resolve("Hello World!");

const promiseHelloWorld = async () => 'Hello World!'

q = promiseHelloWorld().then() // response => 'Hello World!'
q