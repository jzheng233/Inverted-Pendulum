var canvas = document.querySelector('#simulation_canvas');
var ctx = canvas.getContext('2d');
var runner = document.querySelector('#run_button');
//var x_val = document.querySelector('#x_array_length');
//var x_array_val = document.querySelector('#x_array_val');

runner.addEventListener('click', start_simulation);

ctx.beginPath();
ctx.strokeStyle = '#000000';
ctx.lineWidth = 4;
ctx.fillStyle="lightblue";
ctx.fillRect(0, 0, 500, 500);

function clearImage(){
    ctx.clearRect(0, 0, 500, 500);
}

var k = 0;
var w = 100;
var h = 40;
var L = 200;
var y = 300 - h/2;
var mmPixel = 3.7795275591;
var multiplier = 5;
var x_start = 100;

var x_array = [];
var a_array = [];
var display = '';

function scaleToPixel(x_value) {
  fltVal = x_value * 1000 * mmPixel;
  return Math.round(fltVal);
}

function animate(){
    globalID = requestAnimationFrame(animate);
    clearImage();

    var val = x_array[k];
    var ang = a_array[k];
    var theta = multiplier * parseFloat(ang);
    var x_center = parseFloat(val);
    var pixel = scaleToPixel(x_center);
    x = x_start - w/2 + pixel;

//   var display = display.concat(ang,',');
//   $("#x_array_val").text(display);

    ctx.beginPath();
    ctx.fillStyle="green";
    ctx.fillRect(x,y,w,h);

    ctx.beginPath();
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 4;
    ctx.setLineDash([]);
    ctx.moveTo(x + w/2, y);
    x1 = x + w/2 + Math.round(L * Math.sin(theta));
    y1 = y - Math.round(L * Math.cos(theta));
    ctx.lineTo(x1, y1);
    ctx.stroke();

    ctx.beginPath();
    ctx.strokeStyle = 'red';
    ctx.setLineDash([5,3]);
    ctx.lineWidth = 1;
    ctx.moveTo(x + w/2, y);
    ctx.lineTo(x + w/2, y-270);
    ctx.stroke();

    ctx.beginPath();
    ctx.font = "20px Arial";
    ctx.fillText ("Step = "+ k.toString(), 20, 440);
    deg = theta * 180.0/Math.PI;
    disp_angle = "Theta =" + deg.toString();
    ctx.fillText(disp_angle, 20, 480);
    k++;
    if(k >= 4999) {
        cancelAnimationFrame(globalID);
    }
}

function start_simulation() {
    $.post( "/run_simulation", {
    }, function(data, status, resp){
        x_array = data.x_path;
        a_array = data.angle;
        animate();
    });
}
