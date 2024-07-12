//algotihm to use DFT
//a=bi
class Complex {
  constructor(a,b) {
    this.re = a; 
    this.im = b;
    }

add(c) {
  this.re += c.re;
  this.im += c.im;
  }

mult(c) {
  const re = this.re * c.re - this.im * c.im;
  const im = this.re * c.im + this.im * c.re;
  return new Complex (re, im);
  }
}

function dft(x) {
  const X = [];
  const Values = [];
  const N = x.length;
  for (let k = 0; k < N; k++) {
    let sum = new Complex (0, 0);
    for (let n = 0; n < N; n++) {
        const phi = (TWO_PI * K * n) / N;
        const c = new Complex (cos (phi), -sin(phi));
        sum.add(x[n].mult(c));
    }
    sum.re = sum.re/ N;
    sum.im = sum.im / N;
    //get frequency
    let freq = k;
    //get amp
    let amp = sqrt(sum.resum.re + sum.im * sum.im);
    //get phase
    let phase = atan2(sum.im, sum.re);
    X[k] = {re: sum.re, im: sum.im, freq, amp, phase };
    Values[k] = { phase };  
    console.log(Values[k]);
  }
  return X;
}
