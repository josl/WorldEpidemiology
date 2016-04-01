var readline = require('readline');
var fs = require('fs');
var file = 'data/provinces_pop.tsv';
var outA = fs.createWriteStream('data/provinces_A.tsv');
var outB = fs.createWriteStream('data/provinces_B.tsv');
var outC = fs.createWriteStream('data/provinces_C.tsv');
var outD = fs.createWriteStream('data/provinces_D.tsv');
var rl = readline.createInterface({
  input: fs.createReadStream(file),
  // output: out
});
var i = 1;
var header = '';
// Remove header
var linesFile = (10980644 - 1) / 4;

rl.on('line', function (line) {
    var buf4 = new Buffer(line, 'utf8');
    var newLine = buf4.toString('utf8') + '\n';
    if (i === 1){
        process.stdout.write('getting header!' + i + '\n');
        header = newLine;
    }
    if (i <= linesFile) { //  1-13562086
        process.stdout.write('File A...' + i + '\r');
        outA.write(newLine);
    }else if (i > linesFile && i <= linesFile * 2) { //  13562087-27124173
        if (i === linesFile + 2){
            process.stdout.write('\n');
            console.log('Writing header: ' + header);
            outB.write(header);
        }
        process.stdout.write('File B...' + i + '\r');
        outB.write(newLine);
    }else if (i > linesFile * 2 && i <= linesFile * 3) {  //  27124174-40686259
        if (i === (linesFile * 2) + 2){
            process.stdout.write('\n');
            console.log('Writing header: ' + header);
            outC.write(header);
        }
        process.stdout.write('File C...' + i + '\r');
        outC.write(newLine);
    }else if (i > linesFile * 3 && i <= linesFile * 4) { //  40686260-54248345
        if (i === (linesFile * 3) + 2){
            process.stdout.write('\n');
            console.log('Writing header: ' + header);
            outD.write(header);
        }
        process.stdout.write('File D...' + i + '\r');
        outD.write(newLine);
    }else {
        process.stdout.write('\n');
        process.stdout.write('File exceeded...' + i + '\r');
    }
    i+=1;
});

rl.on('close', function () {
    console.log('Let\'s read the file again');
    console.log('Done!');
});
