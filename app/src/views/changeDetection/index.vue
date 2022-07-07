<template>
    <div class="change">
        <Header />
        <div class="main">
            <Menu>
                <div class="lj">
                    <span @click="gotoDetail">了解更多</span>
                    <span @click="showMap" style="margin-left: 50px;">没有遥感图像？</span>
                </div>     
            </Menu>
            <transition appear name="toright">
                <div class="bottom" v-show="isshow">
                    <transition name="disappear">
                        <div class="container" v-show="!isresult">
                            <div class="desc">
                                <div class="tip">
                                    <div class="step">
                                        <TipLine :steps="steps"/>
                                    </div>
                                    <div class="button">
                                        <button @click="start">开始检测</button>
                                    </div>
                                </div>
                            </div>
                            <div class="upimg">
                                <div class="upshow">
                                    <div class="row" :style="{transform: ($store.state.theme === 'light') ? 'translateY(0)' : isreading1 ? 'translateY(0)' : 'translateY(60px)'}">
                                        <div class="upload">
                                            <Upload v-show="!isreading1" :emitName="'showimg1'" />
                                            <transition appear name="toright">
                                                <div class="img" v-show="isreading1">
                                                    <img src="" alt="" ref="readimg1">
                                                </div>
                                            </transition>
                                        </div>
                                        <div class="label" :style="{transform: ($store.state.theme === 'light') ? 'translateY(0)' : isreading1 ? 'translateY(0)' : 'translateY(-30px)'}">
                                            第一时期
                                            <div class="before"></div>
                                            <div class="after"></div>
                                        </div>
                                    </div>
                                    <div class="title">
                                        <img class="nimg" src="../../assets/背景.png" alt="" v-show="!isreading1 && $store.state.theme === 'light'">
                                        <hr v-show="isreading1 && $store.state.theme === 'light'"/>
                                        <transition name="totop">
                                            <div class="but" v-show="isreading1">
                                                <button class="button" @click="reUpload1">重新上传</button>
                                                <input type="file" style="display: none;" accept="image/png" @change="change1" ref="input1" />
                                            </div>
                                        </transition>
                                        <transition name="totop">
                                            <div class="main" v-show="isreading1">
                                                <img src="../../assets/照片.svg" alt="" class="image">
                                                <div class="progress">
                                                    <Progress :current="progress1"/>
                                                </div>
                                            </div>
                                        </transition>
                                    </div>
                                </div>
                                <div class="lod" v-if="loading">
                                    <div class="loadinging">
                                        <div class="loading"></div>
                                    </div>
                                </div>
                            </div>
                            <div class="upimg">
                                <div class="upshow">
                                    <div class="row" :style="{transform: ($store.state.theme === 'light') ? 'translateY(0)' : isreading2 ? 'translateY(0)' : 'translateY(60px)'}">
                                        <div class="upload">
                                            <Upload v-show="!isreading2" :emitName="'showimg2'" />
                                            <transition appear name="toright">
                                                <div class="img" v-show="isreading2">
                                                    <img src="" alt="" ref="readimg2">
                                                </div>
                                            </transition>
                                        </div>
                                        <div class="label" :style="{transform: ($store.state.theme === 'light') ? 'translateY(0)' : isreading2 ? 'translateY(0)' : 'translateY(-30px)'}">
                                            第二时期
                                            <div class="before"></div>
                                            <div class="after"></div>
                                        </div>
                                    </div>
                                    <div class="title">
                                        <img class="nimg" src="../../assets/背景.png" alt="" v-show="!isreading2 && $store.state.theme === 'light'">
                                        <hr v-show="isreading2 && $store.state.theme === 'light'"/>
                                        <transition name="totop">
                                            <div class="but" v-show="isreading2">
                                                <button class="button" @click="reUpload2">重新上传</button>
                                                <input type="file" style="display: none;" accept="image/png" @change="change2" ref="input2" />
                                            </div>
                                        </transition>
                                        <transition name="totop">
                                            <div class="main" v-show="isreading2">
                                                <img src="../../assets/照片.svg" alt="" class="image">
                                                <div class="progress">
                                                    <Progress :current="progress2"/>
                                                </div>
                                            </div>
                                        </transition>
                                    </div>
                                </div>
                                <div class="lod" v-if="loading">
                                    <div class="loadinging">
                                        <div class="loading"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </transition>
                    <transition name="right">
                        <div class="resultmain" v-show="isresult">
                            <div class="detection">
                                <div class="main">
                                    <div class="first showi">
                                        <div class="shw">
                                            <img :src="img1" alt="">
                                            <div class="first1"></div>
                                            <div class="second1"></div>
                                            <div class="three1" v-show="isscan">
                                                <div></div>
                                                <div></div>
                                            </div>
                                        </div>
                                        <!-- <img :src="img1" alt=""> -->
                                        <button @click="reUpload1">重新上传</button>
                                    </div>
                                    <div class="second showi">
                                        <div class="shw">
                                            <img :src="img2" alt="">
                                            <div class="first1"></div>
                                            <div class="second1"></div>
                                            <div class="three1" v-show="isscan">
                                                <div></div>
                                                <div></div>
                                            </div>
                                        </div>
                                        <!-- <img :src="img2" alt=""> -->
                                        <button @click="reUpload2">重新上传</button>
                                    </div>
                                </div>
                            </div>
                            <div class="start">
                                <div class="main">  
                                    <button @click="start">开始检测</button>           
                                    <img src="../../assets/箭头.svg" alt="">
                                </div>
                            </div>
                            <div class="res">
                                <div class="main">
                                    <div class="resimg">
                                        <img :src="resimg1" alt="">
                                        <div class="dow1">
                                            <Download :src="resimg1"/>
                                        </div>
                                        <img :src="resimg2" alt="">
                                        <div class="dow2">
                                            <Download :src="resimg2"/>
                                        </div>
                                        <div class="message">
                                            变化区域个数：<span>{{resstr}}</span> 个 
                                            <button @click="gotoDetail">更多操作</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </transition>
                </div>
            </transition>
            <transition name="slide">
                <div class="detail" v-if="isDetail">             
                    <CDdetail :img1="img1" :img2="img2" :resimg1="resimg2" :resimg2="resimg3" :resnums="resstr"/>   
                </div>
            </transition>
            <transition name="slide">
                <div class="detail" v-if="map">             
                    <Map />   
                </div>
            </transition>
        </div>   
    </div>
</template>

<script>
    import Header from '@/components/header/Header.vue'
    import Menu from '@/components/menu/Menu.vue'
    import Upload from '@/components/upload/Upload.vue'
    import TipLine from './children/TipLine.vue'
    import Progress from '@/components/progress/Progress.vue'
    import CDdetail from './childrenView/CDdetail.vue'
    import Map from '@/components/map/Map.vue'

    import {getCookie} from '@/utils/cookie'
    import {nanoid} from 'nanoid'
    import {
        sedChangeBeforeImg,
        sedChangeAfterImg,
        startDetection
    } from '@/api'
    export default {
        name: 'ChangeDetection',
        components: { 
            Header,
            Menu,
            Upload,
            TipLine,
            Progress,
            CDdetail,
            Map 
        },
        data(){
            return {
                // 控制动画
                isshow: true,
                steps: [
                    {
                        id: 1,
                        tip: '上传同区域的第一个时期的遥感图片'
                    },
                    {
                        id: 2,
                        tip: '上传同区域的第二个时期的遥感图片'
                    },
                    {
                        id: 3,
                        tip: '点击下面的检测按钮'
                    }
                ],
                isreading1: false, // 是否显示要上传的图片
                progress1: 0,      //上传的进度
                img1: '',         // 本地显示的图片
                img1Data: null,    // 要上传的图片详细信息
                id1: '', 
                isreading2: false, // 是否显示要上传的图片
                progress2: 0,
                img2: '',
                img2Data: null,
                isresult: false, // 是否开始检测
                isDetail: false, // 是否显示详细信息
                id2: '',
                isscan: true,
                loading: false,
                resimg1: '',
                resimg2: '',
                resimg3: '',
                resstr: 0,
                map: false,
            }
        },
        activated(){
            // 控制动画
            this.isshow = true
            this.isDetail = false
        },
        mounted() {
            this.$bus.$on('showimg1', (file, data) => {     
                if (getCookie('xmut')) {
                    this.$refs.readimg1.src = file
                    this.img1 = file
                    this.img1Data = data
                    this.isreading1 = true
                    this.submit1()
                } else {
                    this.$router.push({path: '/login'})
                }  
            })
            this.$bus.$on('showimg2', (file, data) => {
                if (getCookie('xmut')) {
                    this.$refs.readimg2.src = file
                    this.img2 = file
                    this.img2Data = data
                    this.isreading2 = true
                    this.submit2()
                } else {
                    this.$router.push({path: '/login'})
                }         
            })
        },
        methods: {
            // 开始检测
            start() {
                if (!this.id1 || !this.id2) {
                    if (!this.id2) {
                        this.$toast.warning('请上传第二张图片')
                    }
                    if (!this.id1) {
                        this.$toast.warning('请上传第一张图片')
                    }
                } else {
                    this.loading = true
                    this.isscan = true
                    const params = {
                        before: this.id1,
                        after: this.id2
                    }
                    startDetection(params).then((response) => {
                        const {resimg1, resimg2, resimg3, nums} = response.data
                        this.resimg1 = resimg1
                        this.resimg2 = resimg2
                        this.resimg3 = resimg3
                        this.resstr = nums
                        this.isresult = true
                        this.isscan = false
                        this.loading = false
                    }, error => {})
                }
            },
            listenProgress1(progressEvent){
                this.progress1 = parseFloat((progressEvent.loaded / progressEvent.total * 100).toFixed(2))
            },
            listenProgress2(progressEvent){
                this.progress2 = parseFloat((progressEvent.loaded / progressEvent.total * 100).toFixed(2))
            },
            submit1(){
                const formData = new FormData()
                formData.append("file", this.img1Data)
                const id = nanoid()
                this.id1 = id
                const params = {
                    id,
                    token: getCookie('xmut')
                }
                sedChangeBeforeImg(formData, this.listenProgress1, params).then((response) => {
                    if (response.data.state) {
                        this.$toast.success('图片上传成功')
                    } else {
                        this.$toast.error('图片上传失败')
                    }
                }, error => {})
            },
            submit2(){
                const formData = new FormData()
                formData.append("file", this.img2Data)
                const id = nanoid()
                this.id2 = id
                const params = {
                    id,
                    token: getCookie('xmut')
                }
                sedChangeAfterImg(formData, this.listenProgress2, params).then((response) => {
                    if (response.data.state) {
                        this.$toast.success('图片上传成功')
                    } else {
                        this.$toast.error('图片上传失败')
                    }
                }, error => {})
            },
            gotoDetail() {
                this.isDetail = true
            },
            change1(event){ 
                let fileReader = new FileReader()
                fileReader.readAsDataURL(event.target.files[0])
                fileReader.onload = () => {
                    this.$refs.readimg1.src = fileReader.result
                    this.img1 = fileReader.result
                }
                this.img1Data = event.target.files[0]
                if (getCookie('xmut')) {
                    this.progress1 = 0
                    this.submit1()
                } else {
                    this.$router.push({path: '/login'})
                }
            },
            change2(event){
                let fileReader = new FileReader()
                fileReader.readAsDataURL(event.target.files[0])
                fileReader.onload = () => {
                    this.$refs.readimg2.src = fileReader.result
                    this.img2 = fileReader.result
                }
                this.img2Data = event.target.files[0]
                if (getCookie('xmut')) {
                    this.progress2 = 0
                    this.submit2()
                } else {
                    this.$router.push({path: '/login'})
                }
            },
            reUpload1(){
                this.$refs.input1.click()
            },
            reUpload2(){
                this.$refs.input2.click()
            },
            showMap() {
                this.map = true
            }
        }
       
    }
</script>

<style lang='less' scoped>
    .change {
        width: 100%;
        height: 100%;
        .main {
            width: 100%;
            height: 88%;
            position: relative;
            .bottom {
                width: 100%;
                height: 72%;
                .container {
                    width: 100%;
                    height: 100%;
                    overflow: hidden;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
            }
            .detail {
                position: absolute;
                width: 100%;
                height: 100%;
                left: 0;
                top: 0;
            }
        }
    }
    .desc {
        width: 390px;
        height: 100%;
        padding: 30px 50px 50px 50px;
        .tip {
            width: 100%;
            height: 100%;
            border-radius: 8px;
            background: var(--change-bg);
            overflow: hidden;
            .step{
                width: 100%;
                height: 80%;
            }
            .button {
                width: 100%;
                height: 20%;
                background-color: var(--change-bt);
                position: relative;
                border-radius: var(--change-ra);
                button {
                    color: white;
                    position: absolute;
                    left: 50%;
                    top: 50%;
                    background-color: transparent;
                    border: none;
                    font-size: 26px;
                    width: 120px;
                    height: 40px;
                    line-height: 40px;
                    text-align: center;
                    transform: translate(-50%, -50%);
                    transition: all .5s;
                    cursor: pointer;
                    &:hover {
                        transform: translate(-50%, calc(-50% - 3px));
                        text-shadow: 0 10px 10px #aeaeae;
                    }
                }
            }
        }
    }

    .lj {
        margin-left: 100px;
        font-size: 17px;
        position: relative;
        height: 20px;
        line-height: 20px;
        // color: var(--menu-message-desc-color);
        margin-top: 4px;
        color: #517FFF;
        cursor: pointer;
        &::before {
            display: block;
            position: absolute;
            content: '';
            width: 10px;
            height: 10px;
            left: -17px;
            top: 25%;
            border-radius: 50%;
            background-color: var(--menu-message-dian-color);
        }
    }

    .upimg {
        flex: 1;
        width: 500px;
        height: 100%;
        padding: 30px 50px 50px 0px;
        position: relative;
        .upshow {
            width: 100%;
            height: 100%;
            border-radius: 8px;
            background: var(--main-bg);
            overflow: hidden;
            .row {
                width: 100%;
                height: 275px;
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
                // z-index: 10;
                .label {
                    position: absolute;
                    right: 35px;
                    top: 11px;
                    width: 85px;
                    height: 28px;
                    font-size: 17px;
                    line-height: 28px;
                    text-align: center;
                    background-color: #7297fe;
                    color: white;
                    .before {
                        position: absolute;
                        top: 0;
                        left: -25px;
                        border-top: 14px solid transparent;
                        border-bottom: 14px solid transparent;
                        border-right: 25px solid #7297fe;

                    }
                    .after {
                        position: absolute;
                        top: 0;
                        right: -20px;
                        border-top: 14px solid #7297fe;
                        border-bottom: 14px solid #7297fe;
                        border-right: 20px solid transparent;
                    }
                }
                .upload {
                    padding-top: 30px;
                    width: 430px;
                    height: 243px;
                    .img {
                        width: 100%;
                        height: 100%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        img {
                            height: 100%;
                        }
                    }
                }
            }
            .title {
                width: 100%;
                height: calc(100% - 275px);
                .nimg {
                    width: 100%;
                    transform: translateY(-35px);
                }
                hr {
                    margin: 0 auto;
                    width: 90%;
                }
                .but {
                    width: 100%;
                    height: 35px;
                    display: flex;
                    justify-content: center;
                    button {
                        width: 90px;
                        height: 35px;
                        border-radius: 5px;
                        border: none;
                        font-size: 16px;
                        color: white;
                        background-color: #7297FE;
                        cursor: pointer;
                        transform: translateY(11px);
                    }
                }
                .main {
                    width: 100%;
                    height: calc(100% - 35px);
                    display: flex;
                    align-items: center;
                    justify-content: center;  
                    .image {
                        width: 40px;
                        margin-right: 10px;
                    }
                    .progress {
                        width: 320px;
                        height: 60px;
                    }
                }              
            }
        }
        .lod {
            width: calc(100% - 50px);
            height: calc(100% - 80px);
            display: flex;
            left: 0;
            top: 30px;
            justify-content: center;
            align-items: center;
            position: absolute;
            // background: rgba(0, 0, 0, 0.2);
            z-index: 10;
            overflow: hidden;
            &::before {
                display: block;
                content: '';
                position: absolute;
                left: 0;
                right: 0;
                width: 100%;
                height: 100%;
                border-radius: 8px;
                background: #2b2b2b;
                opacity: .2;
            }
            .loadinging {
                width: 52px;
                height: 52px;
                animation: rotateing 2.6s linear infinite;
                .loading {
                    width: 100%;
                    height: 100%;
                    border-radius: 50%;
                    border: 5px solid #5e88fe;
                    transition: all .4s;
                    animation: loadinging 1.3s linear infinite;
                }
            }
        }
    }
    
 
    .resultmain {
        width: 100%;
        height: 100%;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .detection {
        width: 400px;
        height: 100%;
        padding: 30px 20px 40px 40px;
        .main {
            width: 100%;
            height: 100%;
            border-radius: 8px;
            background-color: var(--main-bg);
            border: var(--change-res-border);
            overflow: hidden;
            .showi {
                width: 100%;
                height: 50%;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 15px 20px;
                .shw {
                    // background-color: red;
                    width: 177px;
                    height: 177px;
                    position: relative;
                    img {
                        display: block;
                        width: 100%;
                        height: 100%;
                    }
                     .first1 {
                        &::before {
                            position: absolute;
                            left: -5px;
                            top: -5px;
                            content: '';
                            display: block;
                            width: 35px;
                            height: 35px;
                            border-top: 4px solid var(--scan-color);
                            border-left: 4px solid var(--scan-color);
                        }
                        &::after {
                            position: absolute;
                            right: -5px;
                            top: -5px;
                            content: '';
                            display: block;
                            width: 35px;
                            height: 35px;
                            border-top: 4px solid var(--scan-color);
                            border-right: 4px solid var(--scan-color);
                        }
                    }
                    .second1 {
                        &::before {
                            position: absolute;
                            left: -5px;
                            bottom: -5px;
                            content: '';
                            display: block;
                            width: 35px;
                            height: 35px;
                            border-bottom: 4px solid var(--scan-color);
                            border-left: 4px solid var(--scan-color);
                        }
                        &::after {
                            position: absolute;
                            right: -5px;
                            bottom: -5px;
                            content: '';
                            display: block;
                            width: 35px;
                            height: 35px;
                            border-bottom: 4px solid var(--scan-color);
                            border-right: 4px solid var(--scan-color);
                        }
                    }
                    .three1 {
                        position: absolute;
                        left: 0;
                        top: 0;
                        width: 100%;
                        height: 100%;
                        overflow: hidden;
                        div {
                            position: absolute;
                            left: 0;
                            width: 100%;
                            height: 100%;
                            &:nth-child(1) {
                                top: -100%;
                                animation: scan1 2.6s linear infinite;
                                border-bottom: 4px solid var(--scan-line); //rgba(88, 255, 197, .7)
                                background-image: var(--scan-show1);
                            }
                            &:nth-child(2) {
                                top: 100%;
                                border-top: 4px solid var(--scan-line); // var(--scan-color)
                                animation: scan2 2.6s linear 1.3s infinite;
                                background-image: var(--scan-show2);
                            }
                        }
                    }
                }
                // img {
                //     height: 100%;
                // }
                button {
                    width: 85px;
                    height: 32px;
                    border-radius: 5px;
                    border: none;
                    font-size: 16px;
                    color: white;
                    background-color: #7297FE;
                    cursor: pointer;
                    margin-left: 25px;
                }
            }
        }
    }
    

    @keyframes scan1 {
        0% {
            top: -100%;  
        }
        100% {
            top: 100%;
        }
    }
    @keyframes scan2 {
        0% {
            top: 100%;   
        }
        100% {
            top: -100%; 
        }
    }

    .start {
        width: 230px;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        .main {
            width: 180px;
            height: 80px;
            display: flex;
            align-items: center;
            position: relative;
            img {
                width: 100%;
            }
            button {
                position: absolute;
                top: -30px;
                left: 15px;
                width: 90px;
                height: 34px;
                border-radius: 5px;
                border: none;
                font-size: 18px;
                color: white;
                background-color: #08E09F;
                cursor: pointer;
                transition: all .5s;
                &:hover {
                    transform: translateY(-3px);
                }
            }
        }
    }

    .res {
        flex: 1;
        width: 500px;
        height: 100%;
        padding: 30px 45px 40px 0px;
        .main {
            width: 100%;
            height: 100%;
            border-radius: 8px;
            background-color: var(--main-bg);
            position: relative;
            overflow: hidden;
            .resimg {
                width: 100%;
                height: 100%;
                padding: 0px 10px 0px;
                display: flex;
                justify-content: center;
                align-content: center;
                flex-wrap: wrap;
                img {
                    width: 310px;
                    height: 310px;
                    &:nth-child(1) {
                        margin-right: 80px;
                    }
                }
                .dow1 {
                    position: absolute;
                    top: calc((100% - 330px) / 2 - 14px);
                    left: calc((100% - 330px) / 2 + 82px);
                    width: 30px;
                    height: 30px;
                }
                .dow2 {
                    position: absolute;
                    top: calc((100% - 330px) / 2 - 14px);
                    right: calc((100% - 330px) / 2  - 170px);
                    width: 30px;
                    height: 30px;
                }
                .message {
                    width: 100%;
                    height: 60px;
                    padding-left: 75px;
                    margin-top: 10px;
                    line-height: 60px;
                    text-align: left;
                    font-size: 20px;
                    position: relative;
                    font-weight: 700;
                    color: var(--main-font-color);
                    span {
                        color: #7297FE;
                    }
                    &::before {
                        display: block;
                        content: '';
                        position: absolute;
                        bottom: 0;
                        left: 70px;
                        width: calc(100% - 140px);
                        height: 3px;
                        background-color: #7297FE;
                    }
                    button {
                        height: 30px;
                        margin-left: 310px;
                        border-radius: 6px;
                        width: 200px;
                        border: none;
                        color: white;
                        font-size: 18px;
                        line-height: 30px;
                        background: #7297FE;
                    }
                }
            }
            
        }
    }



    .toright-enter-active {
        animation: toright .8s;
    }
    .toright-leave-active {
        animation: toright .8s reverse;
    }
    .totop-enter-active {
        animation: totop .8s;
    }

    @keyframes disappear {
        0% {
            opacity: 1;
            transform: translateX(0);
        }
        100% {
            opacity: 0;
            transform: translateX(100%);
        }
    }
    .disappear-leave-active {
        animation: disappear .8s;
    }

    .right-enter-active {
        animation: toright .4s .8s;
    }

    @keyframes slide {
        0% {
            opacity: 0;
            transform: translate(100%, 100%);
        }
        100% {
            opacity: 1;
            transform: translate(0, 0);
        }
    }
    .slide-leave-active {
        animation: slide .45s reverse;
    }

    .slide-enter-active {
        animation: slide .45s;
    }
    
</style>