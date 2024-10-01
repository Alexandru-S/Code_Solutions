function maximumPerimeterTriangle(sticks: number[]): number[] {
    let maxtriangle: number[] = [-1];
    sticks.sort((a, b) => b - a);
    for (let i = 0; i < sticks.length - 2; i++) {
      if (sticks[i] < sticks[i + 1] + sticks[i + 2]) {
        maxtriangle = [sticks[i + 2], sticks[i + 1], sticks[i]];
        break;
      }
    }
    return maxtriangle;
  }