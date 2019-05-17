(function() {
  
  var canvas = document.getElementById('canvasV'),
  context = canvas.getContext('2d'),
  video = document.getElementById('videoElement'),
  vendorUrl = window.URL || window.webkitURL;
  
  navigator.getMedia =  navigator.getUserMedia ||
  navigator.webkitGetUserMedia ||
  navigator.mozGetuserMedia ||
  navigator.msGetUserMedia;
  
  navigator.getMedia({
    video: true,
    audio: false
  }, function(stream) {
    video.src = vendorUrl.createObjectURL(stream);
    video.play();
  }, function(error) {
    // an error occurred
  } );
  
  video.addEventListener('play', function() {
    draw( this, context, 280, 280 );
  }, false );
  
  function draw( video, context, width, height ) {
    var image, data, i, r, g, b, brightness;
    
    context.drawImage( video, 0, 0, width, height );
    
    image = context.getImageData( 0, 0, width, height );
    data = image.data;
    
    for( i = 0 ; i < data.length ; i += 4 ) {
      r = data[i];
      g = data[i + 1];
      b = data[i + 2];
      
    }
    
    image.data = data;
    
    context.putImageData( image, 0, 0 );
    
    setTimeout( draw, 10, video, context, width, height );
  }
  
} )();