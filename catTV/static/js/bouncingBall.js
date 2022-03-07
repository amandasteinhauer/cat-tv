import Ball from "./Ball.js";

let canvas, ctx, balls, requestID;
const colors = ["brown", "black", "white", "burlywood", "chocolate", "grey"];

var numBalls = 1;
let ballsDisplay = document.getElementById("numBalls")

function startBouncingBallGame() {
  // get the canvas and context
  canvas = document.getElementById("bouncingBallCanvas");
  ctx = canvas.getContext("2d");
  // set the canvas size
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  requestID = window.requestAnimationFrame(update);
  createBalls(numBalls);
  update();
}

function stopBouncingBallGame() {
  window.cancelAnimationFrame(requestID);
}

function moreBalls() {
  if(numBalls < 10){
    numBalls += 1
    ballsDisplay.innerHTML = numBalls
  } 
  
  if(numBalls >= 10){
    document.getElementById("moreBalls").disabled = true;
  }

  if(numBalls >= 1 && document.getElementById("lessBalls").disabled){
    document.getElementById("lessBalls").disabled = false;
  }
}

function lessBalls() {
  if(numBalls >= 1){
    numBalls -= 1
    ballsDisplay.innerHTML = numBalls
  } 

  if(numBalls == 0){
    document.getElementById("lessBalls").disabled = true;
  }

  if(numBalls < 10 && document.getElementById("moreBalls").disabled){
    document.getElementById("moreBalls").disabled = false;
  }
}

document.getElementById("bouncingBallStart").onclick = startBouncingBallGame;
document.getElementById("bouncingBallStop").onclick = stopBouncingBallGame;
document.getElementById("moreBalls").onclick = moreBalls;
document.getElementById("lessBalls").onclick = lessBalls;

function createBalls(numBalls) {
  balls = [];
  for (let i = 0; i < numBalls; i++) {
    balls.push(
      new Ball(
        Math.random() * canvas.width,
        Math.random() * canvas.height,
        {
          width: canvas.width,
          height: canvas.height
        },
        {
          color: colors[Math.floor(Math.random() * colors.length)],
        }
      )
    );
  }
}

function update() {
  // queue the next update
  requestID = window.requestAnimationFrame(() => update());

  // clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // update objects
  balls.forEach((ball) => ball.move());

  // draw objects
  balls.forEach((ball) => ball.draw(ctx));
}
