function init() {
    console.log("Post list page");
}


function showComments(postId) {
    const div = document.getElementById("comments-" + postId);
    if(div.classList.contains('hidden')){
        div.classList.remove('hidden');
    }
    else {
        div.classList.add('hidden')
    }
}



window.onload =init;