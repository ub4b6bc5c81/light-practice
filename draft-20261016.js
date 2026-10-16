// small helpers

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

const uniq = (xs) => [...new Set(xs)];

console.log(sum([1, 2, 3]));
