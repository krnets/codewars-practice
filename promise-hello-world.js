function promiseHelloWorld() {
    return new Promise((resolve, reject) => setTimeout(function () {
        resolve('Hello World!')
    }, 100))
}

async function promiseHelloWorld() {
    return 'Hello World!';
}

const promiseHelloWorld = () => Promise.resolve("Hello World!");

const promiseHelloWorld = async () => 'Hello World!'


q = promiseHelloWorld().then(response => Test.assertEquals('Hello World!', response, 'Simple Single call test'))
q