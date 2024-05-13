
let playButton=document.querySelector(".play-movie")
let video=document.querySelector(".video-container")
let myvideo=document.querySelector("#myvideo")
let closebtn=document.querySelector(".close-video")


playButton.onclick=()=>{
    video.classList.add('show-video');
    // Auto play when click on Button 
    myvideo.play()
};

closebtn.onclick=()=>{
    video.classList.remove('show-video');
    // pause on close video 
    myvideo.pause();
}