let divData, story_text, speech, startBtn, stopBtn;
let bgImage, maskedImage;

function preload() {
    // Load the background image
    bgImage = loadImage('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpTnDS1YjFxlQWvlh2RIMA_HvO-NwaB45qgw&s');
}

function setup() {
    let c = createCanvas(600, 600);
    c.parent('canvas-div');
    divData = document.querySelector("#canvas-div");

    //c.parent('type-div');
    divtype = document.querySelector("#type-div");

    // Create a mask with rounded corners for the background image
    let mask = createGraphics(width, height);
    mask.fill(255);
    mask.noStroke();
    mask.rectMode(CENTER);
    mask.rect(width / 2, height / 2, width - 40, height - 40, 30); // Adjust padding and corner radius

    // Apply the mask to the background image
    maskedImage = bgImage.get(); // Duplicate the image
    maskedImage.mask(mask); // Apply the mask
}

function draw() {
    background(255);

    // Set tint for the image opacity (30% opacity)
    tint(255, 65);

    // Draw the masked image with rounded corners
    image(maskedImage, 20, 20, width - 40, height - 40);

    // Display story text closer to the top of the image
    fill(0);
    textAlign(LEFT, TOP); // Center text horizontally and align to top
    textSize(18);
    textWrap(WORD);
    story_text = divData.dataset.story;
    society_type = divtype.dataset.type;
    print(society_type);
    text(story_text, 60, 60, width - 110, height - 100);}


