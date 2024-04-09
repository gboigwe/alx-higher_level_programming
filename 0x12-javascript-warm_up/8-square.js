#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size) && Number.isInteger(size)) {
    for (let i = 0; i < size; i++) {
        myVar = '';
        for (let j = 0; j < size; j++) myVar += 'X'
            console.log(myVar);
    }
}
else {
    console.log("Missing size");
}
