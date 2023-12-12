#!/usr/bin/node
function secondBiggest(args) {
  if (args.length < 2) {
    console.log(0);
    return;
  }

  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}

const args = [];
for (let i = 2; i < process.argv.length; i++) {
  args.push(parseInt(process.argv[i]));
}
secondBiggest(args);