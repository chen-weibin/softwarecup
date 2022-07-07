<template>
    <div class="all">
        <div class="upload" @click="upload" ref="upload">
            <div class="upld">
                <svg-icon iconClass="upload" className="icon"/>
            </div>
            <div class="title">
                将图片拖到此处，或<span>点击上传</span>
            </div>
            <input type="file" accept="image/png" ref="input" @change="change" />
        </div>
        <div class="tip">
            只能上传png格式的图片
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Upload',
        props: {
            // 触发的事件名称，以此区分不同组件对上传组件的复用
            emitName: {
                type: String,
                default: ''
            }
        },
        methods: {
            upload(){
                this.$refs.input.click()          
            },
            change(event){       
                this.showImg(event.target.files[0])
            },
            // 上传文件
            // submit(file){
            //     const formData = new FormData()
            //     formData.append("file", file)
            //     // this.$emit('update:' + this.emitName, 20)
            //     getdata(formData).then((response) => {
            //         console.log(response.data)
            //         this.$toast.success('上传成功')
            //     }, error => {
            //         this.$toast.error('上传失败')
            //     })
            // },
            // 提取本地文件进行显示
            showImg(file) {
                let fileReader = new FileReader()
                fileReader.readAsDataURL(file)
                fileReader.onload = ()=> {
                    // 触发显示图片
                    this.$bus.$emit(this.emitName, fileReader.result, file)
                    // 同时上传服务器，让父组件上传
                }
                fileReader.onerror = () => {
                    this.$toast.error('图片读取失败')
                }
            }
        },
        mounted(){
            this.$refs.upload.ondrop = (event) => {
                event.preventDefault()
                this.showImg(event.dataTransfer.files[0])
            }
            this.$refs.upload.ondragover = (event) => {
                event.preventDefault()
            }
        }
    }
</script>

<style lang='less' scoped>
    .all {
        background-color: var(--main-bg);
        width: 100%;
        height: 100%;
        padding: 20px 0;
    }
    .upload {
        margin: 0 auto;
        // width: 360px;
        width: calc(100% - 40px);
        // height: 180px;
        height: calc(100% - 16px - 7px);
        border-radius: 8px;
        background-color: var(--main-bg);
        border: 1.5px dashed var(--upload-border);
        cursor: pointer;
        position: relative;
        &:hover {
            border: 1.5px dashed var(--upload-border-hov);
        }
        .upld {
            position: absolute;
            left: 50%;
            top: 40%;
            transform: translate(-50%, -50%);
            .icon {
                width: 67px !important;
                height: 67px !important;
                color: var(--upload-icon);
            }
        }
        .title{
            color: var(--upload-font);
            font-size: 14px;
            text-align: center;
            position: absolute;
            top: 64%;
            width: 100%;
            span {
                color: var(--upload-tit);
                font-style: normal;
            }
        }
    }
    input {
        display: none;
    }
    .tip {
        margin: 0 auto;
        width: calc(100% - 40px);
        height: 16px;
        line-height: 16px;
        font-size: 12px;
        color: var(--upload-font);
        text-align: right;
        margin-top: 7px;
        padding-right: 8px;
        background-color: var(--main-bg);
    }
 
</style>


