const fs = require('fs');
const readline = require('readline');

async function part1() {
    const fileStream = fs.createReadStream('./inputs/input_01.txt');

    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity
    });

    var prev = null;
    var answer = 0;
    for await (const line of rl) {
        if (prev !== null) {
            var current = parseInt(line);
            if (current > prev) answer++;
            prev = current;
        } else {
            prev = parseInt(line);
        }
    }
    console.log(`answer p1: ${answer}`);
}


async function part2() {
    const fileStream = fs.createReadStream('./inputs/input_01.txt');

    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity
    });

    var a = null;
    var b = null;
    var prevsum = null;
    var answer = 0;
    
    for await (const line of rl) {
        if (a === null || b === null) {
            (a === null) ? a = parseInt(line) : b = parseInt(line);
        } else {
            var c = parseInt(line);
            var sum = a + b + c;
            if (prevsum !== null && sum > prevsum) answer++;
            a = b; b = c; prevsum = sum;
        }
    }
    console.log(`answer p2: ${answer}`);
}


part1();
part2();
