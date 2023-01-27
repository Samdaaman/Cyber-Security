

let currentState2 = instance.exports.get_initial_state()
console.log({ currentState: currentState2 });

let password = ''

while (true) {
    let found = false;
    for (let i = 0; i < 128; i ++) {
        const letter = String.fromCharCode(i)
        nextState = instance.exports.check_letter(letter.charCodeAt(0), currentState2);
        if (nextState != 761612191) {
            currentState2 = nextState;
            password += letter
            found = true;
            console.log({ password })
            break
        }
    }
    if (!found) {
        break
    }
}

