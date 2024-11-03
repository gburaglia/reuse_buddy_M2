let divData, story_text, speech, startBtn, stopBtn, society_type, mask;
let bgImage, maskedImage, bgImage_collapsing, bgImage_controlling, bgImage_transforming,bgImage_growing;

function preload() {
    // Load the background images from AWS S3
    bgImage_growing = loadImage('https://ai4dm.s3.us-east-1.amazonaws.com/growing.jpeg');
    bgImage_collapsing = loadImage('https://ai4dm.s3.us-east-1.amazonaws.com/collapsing.jpeg');
    bgImage_controlling = loadImage('https://ai4dm.s3.us-east-1.amazonaws.com/controlling.jpeg');
    bgImage_transforming = loadImage('https://ai4dm.s3.us-east-1.amazonaws.com/transforming.jpeg');
}

function setup() {
    let c = createCanvas(600, 600);
    c.parent('canvas-div');
    divData = document.querySelector("#canvas-div");

    divType = document.querySelector("#type-div");

    // Create a mask with rounded corners for the background image
    mask = createGraphics(width, height);
    mask.fill(255);
    mask.noStroke();
    mask.rectMode(CENTER);
    mask.rect(width / 2, height / 2, width - 40, height - 40, 30); // Adjust padding and corner radius
}

function draw() {
    background(255);

    // Set tint for the image opacity (less than 30% opacity)
    tint(255, 65);
    
    fill(0);
    textAlign(LEFT, TOP); // Center text left and align to top
    textSize(18);
    textWrap(WORD);
    story_text = divData.dataset.story;
    society_type = divType.dataset.type;
    society_type = trim(society_type);
    display_image();
    text(story_text, 60, 60, width - 110, height - 100);
    }

function selectImage(){
    //Switch statement to display correct image based on future society type
    switch (society_type) {
        case "Growing":
          bgImage = bgImage_growing;
          break;
        case "Collapsing":
          bgImage = bgImage_collapsing;
          break;
        case "Controlling":
          bgImage = bgImage_controlling;
          break;
        case "Transforming":
          bgImage = bgImage_transforming; 
          break;
    }
}

function display_image(){
    selectImage();
    //Draw the masked image with rounded corners
    //Apply the mask to the background image selected
     maskedImage = bgImage.get(); //Duplicate the image
     maskedImage.mask(mask); //Apply the mask
    image(maskedImage, 20, 20, width - 40, height - 40);
}


