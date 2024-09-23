/* 보드게임판 js */
/* story 부분 */
function showStory(element){
    var popup = document.getElementById("story-popup");
    var popupImg = document.getElementById("popup-img");

    var uploadImage = "{{ upload_img|escape.js }}";

    if (uploadImage) {
        popupImg.src = uploadImage;
    }else{
        var characterImage = element.querySelector('img').getAttribute('src');
        popupImg.src = characterImage;  // Display the character image instead
    }
    popup.style.display = "block";  // Open the popup
}
function closePopUp(){
    var popup = document.getElementById("story-popup");
    popup.style.display = "none";
}
function showUploadForm(event){
    event.stopPropagation();
    document.getElementById('upload-form').style.display = 'block';
}
function closeForm() {
    document.getElementById('upload-form').classList.remove('active');
}

/* 게임판 부분 */
document.addEventListener('DOMcontentLoaded', function() {
    const gameBoard = document.getElementById('game-board');
    const du = parseInt(gameBoard.dataset.duration, 10);

    const rows = Math.ceil(du/4);

    for (let i=0; i<rows; i++) {    // 행 생성
        const row = document.createElement('div');
        row.className = 'board-row';

        for (let j=0; j<4; j++) {   // 각 행에 칸 4개 생성
            if (i*4+j < du) {
                const space = document.createElement('div');
                space.className = 'space'
                row.appendChild(space);
            }
        }

        gameBoard.appendChild(row); //  gameBoard에 행 추가
    }
});