// 页面最大化
export function requestFullScreen(element){
    let docElm = element
    if(!docElm){
        // 如果没有传入要全屏显示的元素，默认整个界面
        docElm = document.documentElement;
    }
    if(docElm.requestFullscreen){
        docElm.requestFullscreen()
    } else if (docElm.msRequestFullscreen) {
        docElm.msRequestFullscreen();
    } else if (docElm.mozRequestFullScreen) {
        docElm.mozRequestFullScreen();
    } else if (docElm.webkitRequestFullScreen) {
        docElm.webkitRequestFullScreen();
    }
}

// 退出最大化
export function exitFullScreen(){
    if(document.fullscreenElement){
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
            document.webkitCancelFullScreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen()
        }
    }  
}