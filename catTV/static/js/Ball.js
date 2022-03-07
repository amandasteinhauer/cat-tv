export class Ball {
  constructor(x = 0, y = 0, sceneProps, props) {
    this.props = {
      radius: 20,
      startVelX: Math.floor(Math.random() * 5),
      startVelY: Math.floor(Math.random() * 3),
      ...props,
    };
    this.sceneProps = sceneProps;

    this.x = x;
    this.y = y;
    this.velX = this.props.startVelX;
    this.velY = this.props.startVelY;
  }

  draw(ctx) {
    const { x, y, props } = this;

    ctx.save();
    ctx.beginPath();
    ctx.fillStyle = props.color;
    ctx.arc(x, y, props.radius, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  move() {
    const { props, sceneProps } = this;

    // bottom bound / floor
    if (this.y + props.radius >= sceneProps.height) {
      this.velY = 0 - this.velY;
    }

    // top bound / ceiling
    if (this.y - props.radius <= 0) {
      this.velY = 0 - this.velY;
    }

    // left bound
    if (this.x - props.radius <= 0) {
      this.velX = 0 - this.velX;
    }
    // right bound
    if (this.x + props.radius >= sceneProps.width) {
      this.velX = 0 - this.velX;
    }

    // update position
    this.x += this.velX;
    this.y += this.velY;
  }
}

export default Ball;
