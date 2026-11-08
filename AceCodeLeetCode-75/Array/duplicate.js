function duplicate (arr) {
    let dup = false;
    if (arr.length == 1) return dup;

    let left = 0;
    let newarr = arr.sort((a, b) => a - b);
    console.log(newarr);
    for (let right = left + 1; right < newarr.length; right++) {
        if (newarr[right] == newarr[left]) {
           dup = true;
           console.log(dup);
        } else {
            left = right
        }
    }

    return dup;
}

function duplicate (newarr) {
    let arr = []
    for (let i = 0; i < newarr.length; i++) {
       if (arr.includes(newarr[i])) {
         return true;
       } else {
        arr.push(newarr[i]);
       }
    }

    return false;
}

console.log("I am answer ", duplicate([7, 1, 5, 3, 6, 9, 4]));

