const lines = [
  "Retrieval over real documents",
  "Voice agents with evals and traces",
  "Vision systems for the factory floor",
  "Python · SQL · LLMs",
];

const typed = document.querySelector("#typed");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function wait(ms) {
  return new Promise((resolve) => {
    window.setTimeout(resolve, ms);
  });
}

async function typeLine(line) {
  const step = Math.max(16, Math.round(2800 / line.length));
  typed.textContent = "";
  for (const character of line) {
    typed.textContent += character;
    await wait(step);
  }
  await wait(800);
}

async function run() {
  let index = 0;
  while (true) {
    await typeLine(lines[index % lines.length]);
    index += 1;
  }
}

if (reduceMotion) {
  typed.textContent = lines.join("   ·   ");
} else {
  run();
}
