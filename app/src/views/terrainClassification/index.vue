<template>
    <div class="terrain">
        <Header />
        <div class="main">
            <Menu>
                <div class="lj">
                    <span @click="gotoDetail">了解更多</span>
                    <span @click="showMap" style="margin-left: 50px;">没有遥感图像？</span>
                </div> 
            </Menu>
            <transition appear name="toright">
                <div class="content" v-show="isshow">
                    <div class="left">
                        <div class="text">
                            <div class="upload" :style="{transform: isreading ? 'translateY(28px)' : 'translateY(0)'}">
                                <Upload v-show="isreading" :emitName="'terrainClassification'"/>
                                <transition appear name="toright">
                                    <div v-show="!isreading" class="img">
                                        <img ref="terrainClassificationImg" src="" alt="">
                                        <div class="first"></div>
                                        <div class="second"></div>
                                        <div class="three" v-show="isscan">
                                            <div></div>
                                            <div></div>
                                        </div>
                                    </div>
                                </transition>
                            </div>
                            <div class="sumbit">
                                <div class="reup">
                                    <transition appear name="toright">
                                        <button v-show="!isreading" @click="reUpload">重新上传</button>
                                    </transition>
                                    <input type="file" style="display: none;" accept="image/png" @change="change" ref="input" />
                                </div>
                                <div class="start">
                                    <button @click="startTerrainClassification">开始分类</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="right">
                        <div class="text">
                            <div class="pandas" v-if="!resimg && !loading">
                                <div class="moun">
                                    <img src="../../assets/北极地图.png" alt="" class="map">
                                </div>         
                                <div class="show">
                                    <img src="../../assets/北极熊.png" alt="" class="bear">
                                </div>
                                <div class="tip">上传图片试试吧! !</div>
                            </div>
                            <div class="lod" v-show="loading">
                                <div class="loadinging">
                                    <div class="loading"></div>
                                </div>
                            </div>
                            <div class="res" v-show="resimg && !loading">
                                <div class="left1">
                                    <img :src="resimg" alt="" class="imgg">
                                    <div class="dow">
                                        <Download :src="resimg"/>
                                    </div>
                                </div>
                                <div class="tabel">
                                    <div class="title">分类标记</div>
                                    <ul>
                                        <li>
                                            <span class="first top">土地类型</span>
                                            <span class="second top">颜色</span>
                                        </li>
                                        <li>
                                            <span class="first">林地</span>
                                            <span class="second">
                                                <span class="lindi" v-if="leixing.lindi"></span>
                                                <span v-else>未检测到林地</span>
                                            </span>
                                        </li>
                                        <li>
                                            <span class="first">耕地</span>
                                            <span class="second">
                                                <span class="gengdi" v-if="leixing.gengdi"></span>
                                                <span v-else>未检测到耕地</span>
                                            </span>
                                        </li>
                                        <li>
                                            <span class="first">建筑</span>
                                            <span class="second">
                                                <span class="jianzu" v-if="leixing.jianzu"></span>
                                                <span v-else>未检测到建筑</span>
                                            </span>
                                        </li>
                                        <li>
                                            <span class="first">其他</span>
                                            <span class="second">
                                                <span class="qita" v-if="leixing.qita"></span>
                                                <span v-else>未检测到其他</span>
                                            </span>
                                        </li>
                                    </ul>
                                    <div @click="gotoDetail" class="button">
                                        <span>更多详情</span>
                                        <svg-icon iconClass='detail' className="ic"></svg-icon>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
            </transition>
            <transition name="slide">
                <div class="detail" v-if="isDetail">             
                    <Detail :img='img' :resimg='resimg' :resdata="resData"/>   
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
    import {getCookie} from '@/utils/cookie'
    import {getTerrainClassification} from '@/api'
    import {nanoid} from 'nanoid'
    import Detail from './children/Detail.vue'
    import Map from '@/components/map/Map.vue'
    export default {
        name: 'TerrainClassification',
        components: {
            Menu,
            Header,
            Upload,
            Detail,
            Map
        },
        data(){
            return {
                isshow: true,
                isreading: true, // 是否显示要上传的图片
                isscan: true,         // 扫描
                imgData: null,    // 要上传的图片详细信息
                resimg: '', //返回的结果图片
                img: '',
                loading: false,
                leixing: {
                    lindi: false,
                    gengdi: false,
                    jianzu: false,
                    qita: false,
                },
                isDetail: false,
                map: false,
                resData: {},
            }
        },
        activated(){
            this.isshow = true
            this.isDetail = false
        },
        mounted(){
            this.$bus.$on('terrainClassification', (file, data) => {
                this.$refs.terrainClassificationImg.src = file
                this.isreading = false
                this.img = file
                this.imgData = data
            })
        },
        methods: {
            startTerrainClassification(){
                if (this.imgData) { 
                    const cookie = getCookie('xmut')
                    if (cookie) {
                        this.loading = true
                        const formData = new FormData()
                        formData.append("file", this.imgData)
                        const params = {
                            id: nanoid(),
                            token: cookie
                        }
                        getTerrainClassification(formData, params).then((response) => {
                            const {lingdi, gendi, jianzhu, qita} = response.data
                            this.resData = response.data
                            this.leixing.lindi = lingdi.ishave
                            this.leixing.gengdi = gendi.ishave
                            this.leixing.jianzu = jianzhu.ishave
                            this.leixing.qita = qita.ishave
                            this.resimg = response.data.resimg
                            this.isscan = false
                            this.loading = false
                        }, error => {})
                    } else {
                        this.$router.push({path: '/login'})
                    }
                    
                } else {
                    this.$toast.warning('请上传要分类的图片')
                }
            },
            change(event){ 
                this.isscan = true 
                let fileReader = new FileReader()
                fileReader.readAsDataURL(event.target.files[0])
                fileReader.onload = () => {
                    this.$refs.terrainClassificationImg.src = fileReader.result
                    this.img = fileReader.result
                }
                this.imgData = event.target.files[0]
            },
            reUpload(){
                this.$refs.input.click()
            },
            gotoDetail() {
                this.isDetail = true
            },
            showMap() {
                this.map = true
            }
        }
    }
</script>

<style lang='less' scoped>
    .terrain{
        width: 100%;
        height: 100%;
        .main {
            width: 100%;
            height: 88%;
            position: relative;
            .content {
                width: 100%;
                height: 72%;
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

     .left {
        float: left;
        width: 420px;
        height: 100%;
        padding: 30px 0px 50px 50px;
        .text {
            width: 100%;
            height: 100%;
            border-radius: 8px;
            overflow: hidden;
            background: var(--main-bg);
            .upload {
                width: 100%;
                height: 243px;
                display: flex;
                justify-content: center;
                align-items: center;
                .img {
                    position: relative;
                    width: 220px;
                    height: 220px;
                    img {
                        display: block;
                        height: 100%;
                        width: 100%;
                        border: none;
                    }
                    .first {
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
                    .second {
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
                    .three {
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
            }
            .sumbit {
                width: 100%;
                height: calc(100% - 243px);
                .reup {
                    width: 100%;
                    height: 35px;
                    display: flex;
                    justify-content: center;
                    button {
                        width: 90px;
                        height: 35px;
                        color: white;
                        border-radius: 5px;
                        border: none;
                        font-size: 16px;
                        cursor: pointer;
                        background-color: #7297FE;
                        transform: translateY(9px);
                    }
                }
                .start {
                    width: 100%;
                    height: calc(100% - 35px - 30px);
                    margin-top: 30px;
                    background-color: var(--change-bt);
                    border-radius: var(--change-ra);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    button {
                        width: 120px;
                        height: 40px;
                        border: none;
                        font-size: 29px;
                        line-height: 40px;
                        color: white;
                        background-color: transparent;
                        cursor: pointer;
                        transition: all .5s;
                        &:hover {
                            transform: translateY(-3px);
                            text-shadow: 0 10px 10px #aeaeae;
                        }
                    }
                }
            }
        }
    }

    .right {
        float: right;
        width: calc(100% - 420px);
        height: 100%;
        padding: 30px 50px 50px 50px;
        .text {
            width: 100%;
            height: 100%;
            border-radius: 8px;
            background: var(--main-bg);

            .lod {
                width: 100%;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
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
            .res {
                width: 100%;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                .left1 {
                    width: 50%;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    position: relative;
                    img {
                        width: 330px;
                        height: 330px;
                    }
                    .dow {
                        position: absolute;
                        top: calc((100% - 330px) / 2 + 5px);
                        right: calc((100% - 330px) / 2 + 7px);
                        width: 30px;
                        height: 30px;
                    }
                }
                .tabel {
                    width: 50%;
                    height: 100%;
                    position: relative;
                    .title {
                        width: 100%;
                        height: 50px;
                        line-height: 50px;
                        text-align: center;
                        color: var(--main-font-color);
                        font-size: 21px;
                        font-weight: 700;
                        padding-right: 85px;
                        margin-top: 30px;
                    }
                    ul {
                        list-style: none;
                        width: 100%;
                        padding-top: 20px;
                        height: calc(100% - 110px);
                        overflow-y: auto;
                        padding-right: 85px;
                        &::-webkit-scrollbar {
                            display: none;
                        }
                        li {
                            width: 100%;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            cursor: default;
                            span {
                                height: 40px;
                                color: var(--main-font-color);
                                font-size: 18px;
                                line-height: 40px;
                                padding-left: 7px;
                                text-align: center;
                            }
                            .lindi {
                                display: block;
                                margin: 6px auto;
                                width: 70px;
                                height: 26px;
                                background: rgb(60, 0, 255);
                            }
                            .gengdi {
                                display: block;
                                margin: 6px auto;
                                width: 70px;
                                height: 26px;
                                background: rgb(255, 222, 0);
                            }
                            .jianzu {
                                display: block;
                                margin: 6px auto;
                                width: 70px;
                                height: 26px;
                                background: rgb(30, 255, 142);
                            }
                            .qita {
                                display: block;
                                margin: 6px auto;
                                width: 70px;
                                height: 26px;
                                background: rgb(255, 0, 0);
                            }
                            &:hover {
                                background-color: #d5d5d5 !important;
                            }
                            .top {
                                font-weight: 700;
                                font-size: 19px;
                                color: var(--main-font-color) !important;
                                background-color: #6a92ff;
                            }
                            .first {
                                width: 100px;
                                flex: 1;
                            }
                            .second {
                                width: 200px;
                            }
                            &:nth-child(odd) {
                                background-color: rgb(247, 247, 247);
                            }
                            &:nth-child(even) {
                                background-color: #e5e5e5;
                            }
                        }
                    }
                    .button {
                        position: absolute;
                        right: 0;
                        bottom: 40px;
                        height: 30px;
                        margin-right: 85px;
                        text-align: center;
                        color: var(--main-font-color);
                        font-size: 18px;
                        line-height: 30px;
                        cursor: pointer;
                        transition: all .5s;
                        &:hover {
                            transform: translateY(-2px);
                            color: #517FFF;
                        }
                        .ic {
                            width: 22px !important;
                            height: 22px !important;
                            color: inherit;
                        }
                    }
                }
            }
        }
    }

    .pandas {
        width: 100%;
        height: 100%;
        position: relative;
        .tip {
            width: 0px;
            height: 30px;
            line-height: 30px;
            overflow: hidden;
            font-size: 15px;
            left: 60%;
            top: 68%;
            position: absolute;
            color: #638cff;
            letter-spacing: 4px;
            animation: fontmove 2s linear 3s infinite;;
        }
        .moun {
            width: 100%;
            height: 336px;
            position: absolute;
            overflow: hidden;
            left: 0;
            bottom: 0;
            .map {
                position: absolute;
                width: 7680px;
                height: 336px;
                left: 0;
                top: 0;
                animation: mounmove 13s linear infinite; //13
            }
        }
        .show {
            width: 200px;
            height: 100px;
            overflow: hidden;
            position: absolute;
            left: 0;
            bottom: 6%;
            animation: bearmove 3.5s linear forwards;
            .bear {
                position: absolute;
                width: 1600px;
                height: 100px;
                left: 0;
                top: 0;
                animation: run 1s steps(8) infinite;
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
    @keyframes bearmove{
        0% {
            left: 0;
        }
        100% {
            left: 50%;
            transform: translateX(-50%);
        }
    }
    @keyframes fontmove{
        0% {
            width: 0px;
            // color: #517FFF;
        }
        100% {
            width: 200px;
            // color: #08E09F;
        }
    }

    @keyframes run {
        0% {
            left: 0;
        }
        100% {
            left: -1600px;
        }
    }
    @keyframes mounmove{
        0% {
            left: 0;
        }
        100% {
            left: -3840px;
        }
    }

    .toright-enter-active {
        animation: toright .8s;
    }
    .toright-leave-active {
        animation: toright .8s reverse;
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

    @keyframes upbottom {
        0% {
            top: 0;
        }
        100% {
            top: calc(220px - 3.5px);
        }
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