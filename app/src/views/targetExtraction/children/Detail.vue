<template>
    <div class="detaill">
        <div class="top">
            <div class="logolg">
                <img src="../../../assets/理工.png" alt="" class="lg">
            </div>
            <div class="title">
                |&nbsp;&nbsp;目标提取
            </div>
            <div class="returnbef">
                <span @click="returnHome">返回上一级</span>
            </div>
            <div class="returnhome">
                <span @click="returnMain">返回主页</span>
            </div>      
        </div>
        <div class="bottom">
            <div class="left">
                <div class="tit">上传示例</div>
                <div class="con">
                    <div class="item" v-for="(item, index) in showData" :key="index" :class="current === index ? 'current' : ''" @click="changeCurrent(index)">
                        <!-- <div class="time">dkfjkdfjk</div> -->
                        <div class="image">
                            <img :src="item.resimg1" alt="">
                        </div>
                        <div class="bot"></div>
                    </div>
                </div>
            </div>
            <div class="center">
                <div class="show" ref="show">
                    <div class="before" ref="imgup">
                        <img :src="showData.length ? showData[current].resimg1 : ''" alt="" class="img" >
                    </div>
                    <div class="line" ref="line">
                        <div class="lef">
                            <img src="../../../assets/left.svg" alt="" class="ri">
                            <img src="../../../assets/right.svg" alt="" class="ri">
                        </div>
                    </div>
                    <div class="after">
                        <img :src="showData.length ? showData[current].resimg2 : ''" alt="" class="img">
                    </div>
                    <div class="fir">
                        提取前
                    </div>
                    <div class="sec">
                        提取后
                    </div>
                </div>
            </div>
            <div class="right">
                <div class="con">
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;遥感图像目标提取是指单幅图像或序列图像中将感兴趣的目标与背景分割开来，
                    从图像中识别和解译有意义的物体实体而提取不同的图像特征的操作。<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在本目标提取中，提取的是道路信息。
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {TargetExtractionExanple} from '@/api'
    export default {
        name: 'Detail',
        data() {
            return {
                current: 0,
                showData: [],
            }
        },
        props: ['res', 'pre'],
        methods: {
            returnHome(){
                this.$parent.isDetail = false
            },
            returnMain() {
                this.$parent.isDetail = false
                this.$router.push({path: '/home'})
            },
            // 40  664
            setLine(left){
                if (left >= 40 && left <= 664) {
                    this.$refs.line.style.left = left + 'px'
                    this.$refs.imgup.style.width = left + 'px'
                }     
            },
            changeCurrent(index) {
                this.current = index
            }
        },
        mounted() {  
            TargetExtractionExanple().then((res) => {
                const {data} = res.data
                for (let i = 0; i < data.length; i++) {
                    this.showData.push(data[i])          
                }
            }, error => {})
            
            this.$refs.show.onmousedown = (e) => {
                const x = e.clientX + document.body.scrollLeft - this.$refs.show.offsetLeft
                const y = e.clientY + document.body.scrollTop - this.$refs.show.offsetTop - 50
                const left = parseInt(window.getComputedStyle(this.$refs.line, null).getPropertyValue("left"))
                if (x >= left - 30 && x < left + 3 + 30) {
                    if (y < 324 || y > 384) {
                        if (x >= left && x <= left + 3) {
                            this.$refs.show.onmousemove = (e)=>{
                                const newX = e.clientX + document.body.scrollLeft - this.$refs.show.offsetLeft
                                this.setLine(newX)
                            }
                            this.$refs.show.onmouseleave = ()=>{
                                this.$refs.show.onmousemove = null
                            }
                            this.$refs.show.onmouseup = ()=>{
                                this.$refs.show.onmousemove = null
                            }
                        }
                    } else {
                        this.$refs.show.onmousemove = (e)=>{
                            const newX = e.clientX + document.body.scrollLeft - this.$refs.show.offsetLeft
                            this.setLine(newX)
                        }
                        this.$refs.show.onmouseleave = ()=>{
                            this.$refs.show.onmousemove = null
                        }
                        this.$refs.show.onmouseup = ()=>{
                            this.$refs.show.onmousemove = null
                        }
                    }
                }
            }           
        },
        watch: {
            res: {
                immediate: true,
                handler(){
                    if (this.res) {
                        const len = this.showData.length
                        if (len === 5) {
                            this.showData.unshift({resimg1: this.pre, resimg2: this.res})
                        } else {
                            this.showData[0] = {resimg1: this.pre, resimg2: this.res}
                        }
                    }
                }
            }
        },
        
    }
</script>

<style lang='less' scoped>
    .detaill {
        width: 100%;
        height: 100vh;
        position: absolute;
        left: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.8);
        z-index: 9999;
        .bottom {
            width: 100%;
            height: calc(100% - 50px);
            position: relative;
        }
    }

    .top {
        width: 100%;
        height: 50px;
        background-color: #000000;
        .logolg {
            float: left;
            margin-left: 40px;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            .lg {
                width: 35px;
                height: 35px;
            }
        }
        .title {
            float: left;
            width: 125px;
            height: 50px;
            line-height: 50px;
            color: white;
            font-weight: 700;
            font-size: 21px;
            text-align: center;
        }
        .returnbef{
            float: right;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            span {
                height: 28px;
                width: 80px;
                font-weight: 700;
                color: white;
                line-height: 28px;
                text-align: center;
                margin-right: 30px;
                cursor: default;
            }
        }
        .returnhome{
            float: right;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            span {
                height: 28px;
                width: 80px;
                font-weight: 700;
                color: white;
                line-height: 28px;
                text-align: center;
                margin-right: 15px;
                cursor: default;
            }
        }
    }

    .left {
        position: absolute;
        left: 0;
        top: 0;
        height: calc(100% - 50px);
        width: 400px;
        display: flex;
        justify-content: center;
        align-items: center;
        .tit {
            width: 100%;
            height: 40px;
            position: absolute;
            top: 12px;
            left: 0;
            color: white;
            line-height: 40px;
            text-align: center;
            font-size: 20px;
            font-weight: 700;
        }
        .con {
            width: 230px;
            height: 550px;
            overflow-y: auto;
            padding: 5px 15px;
            &::-webkit-scrollbar {
                display: none;
            }
            .item {
                width: 200px;
                height: 180px;
                margin-bottom: 70px;
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                &::before {
                    display: block;
                    position: absolute;
                    content: '';
                    width: 20px;
                    height: 20px;
                    left: -3.5px;
                    top: -3.5px;
                    border-top: 3.5px solid rgb(0, 247, 255);
                    border-left: 3.5px solid rgb(0, 247, 255);
                }
                &::after {
                    display: block;
                    position: absolute;
                    content: '';
                    width: 20px;
                    height: 20px;
                    right: -3.5px;
                    top: -3.5px;
                    border-top: 3.5px solid rgb(0, 247, 255);
                    border-right: 3.5px solid rgb(0, 247, 255);
                }
                .time {
                    width: 100%;
                    height: 15px;
                    color: white;
                    line-height: 15px;
                    text-align: center;
                    overflow: hidden;
                    font-size: 14px;
                }
                .image {
                    // width: 100%;
                    // height: calc(100% - 15px);
                    // display: flex;
                    // justify-content: center;
                    // align-items: center;
                    img {
                        width: 160px; //155
                        height: 160px;
                    }
                }
                .bot {
                    &::before {
                        display: block;
                        position: absolute;
                        content: '';
                        width: 20px;
                        height: 20px;
                        left: -3.5px;
                        bottom: -3.5px;
                        border-bottom: 3.5px solid rgb(0, 247, 255);
                        border-left: 3.5px solid rgb(0, 247, 255);
                    }
                    &::after {
                        display: block;
                        position: absolute;
                        content: '';
                        width: 20px;
                        height: 20px;
                        right: -3.5px;
                        bottom: -3.5px;
                        border-bottom: 3.5px solid rgb(0, 247, 255);
                        border-right: 3.5px solid rgb(0, 247, 255);
                    }
                }
            }
            .current {
                box-shadow: 3px 3px 6px 2px #7ccccf;
            }
        }
    }

    .center {
        margin: 0 auto;
        width: 708px;
        height: calc(100% - 50px);
        .img {
            width: 708px;
            height: 708px;
            -webkit-user-drag: none;
        }
        .show {
            width: 708px;
            height: 708px;
            position: relative;
            margin: 0 auto;
            .before {
                position: absolute;
                height: 708px;
                width: 354px;
                left: 0;
                top: 0;
                overflow: hidden;
                z-index: 10;
            }
            .after {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
            }
            .line {
                position: absolute;
                top: 0;
                left: 354px;
                width: 3px;
                height: 708px;
                z-index: 20;
                background-color: #fff;
                cursor: move;
                .lef {
                    position: absolute;
                    left: -30px;
                    top: calc(50% - 30px);
                    width: 63px;
                    height: 60px;
                    border-radius: 50%;
                    border: 3px solid white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    .ri {
                        width: 30px;
                        -webkit-user-drag: none;
                    }
                }
            }
            .fir {
                position: absolute;
                left: 40px;
                bottom: 80px;
                color: white;
                z-index: 30;
                font-weight: 700;
                font-size: 28px;
                
            }
            .sec {
                position: absolute;
                right: 40px;
                bottom: 80px;
                color: white;
                z-index: 30;
                font-weight: 700;
                font-size: 28px;
            }
        }
    }

    .right {
        position: absolute;
        top: 0;
        right: 0;
        width: 400px;
        height: calc(100% - 50px);
        display: flex;
        justify-content: center;
        align-items: center;
        .con {
            border-radius: 8px;
            width: 280px;
            height: 250px;
            padding: 20px 19px;
            color: white; //#abd4fd
            font-size: 18px;
            background-color: #0F3A65;
        }
    }
</style>