<template>
    <div class="container" @click="download">
        <svg-icon iconClass="download" className="iocn"></svg-icon>
    </div>
</template>

<script>
    export default {
        name: 'Download',
        props: {
            src: {
                type: String,
                default: ''
            }
        },
        methods: {
            download() {
                let image = new Image();
                image.setAttribute("crossOrigin", "anonymous");
                image.src = this.src;
                image.onload = () => {
                    let canvas = document.createElement("canvas");
                    canvas.width = image.width;
                    canvas.height = image.height;
                    let ctx = canvas.getContext("2d");
                    ctx.drawImage(image, 0, 0, image.width, image.height);
                    canvas.toBlob(blob => {
                        let url = URL.createObjectURL(blob);
                        // 用完释放URL对象
                        let eleLink = document.createElement("a");
                        eleLink.download = '下载.png';
                        eleLink.href = url;
                        eleLink.click();
                        eleLink.remove();
                        URL.revokeObjectURL(url);
                    })
                }
   
            }
        }
    }
</script>

<style lang='less' scoped>
    .container {
        width: 30px;
        height: 30px;     
        .iocn {
            width: 100% !important;
            height: 100% !important;
            color: rgb(106, 255, 205);
        }
        &:hover .iocn{
            color: rgb(0, 255, 170);
        }
    }
</style>