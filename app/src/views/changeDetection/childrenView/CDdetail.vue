<template>
    <div class="detaill">
        <div class="top">
            <div class="logolg">
                <img src="../../../assets/理工.png" alt="" class="lg">
            </div>
            <div class="title">
                |&nbsp;&nbsp;变化检测
            </div>
            <div class="returnbef">
                <span @click="returnHome">返回上一级</span>
            </div>
            <div class="returnhome">
                <span @click="returnMain">返回主页</span>
            </div>
            
        </div>
        <div class="bottom">
            <div class="show" ref="show">
                <div class="before" ref="imgup">
                    <img :src="showData.length ? (openeyes ? showData[current].resimg4 : showData[current].resimg1) : ''" alt="" class="img" >
                </div>
                <div class="line" ref="line">
                    <div class="lef">
                        <img src="../../../assets/left.svg" alt="" class="ri">
                        <img src="../../../assets/right.svg" alt="" class="ri">
                    </div>
                </div>
                <div class="fir">
                    前时相
                </div>
                <div class="sec">
                    后时相
                </div>
                <div class="after">
                    <img :src="showData.length ? (openeyes ? showData[current].resimg5 : showData[current].resimg2) : ''" alt="" class="img">
                </div>
            </div> 
            <div class="bolef">
                <div class="tit">上传示例</div>
                <div class="con">
                    <div class="item" v-for="(item, index) in showData" :key="index" :class="current === index ? 'current' : ''" @click="changeCurrent(index)">
                        <!-- <div class="time">2021/2/23 - 2022/3/03</div> -->
                        <div class="image">
                            <img :src="item.resimg1" alt="">
                            <img :src="item.resimg2" alt="">
                        </div>                     
                        <div class="bot"></div>
                    </div>
                </div>
            </div>
            <div class="borig">
                <div class="describute">
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;遥感图像变化检测一般是指以一个时相的遥感图像为参考，
                    检测出另外时相相对参考图像的差异。随着地球信息科学的发展和应用需求的多样化，
                    变化检测的研究内容得到了极大的丰富，参考数据不再局限于遥感图像，
                    也可以是GIS数据、地形图以及其他地球空间信息产品。<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;比较全面的遥感图像变化检测概念可以理解为：
                    遥感图像变化检测是一门根据遥感图像和参考数据不同时相的观测来提取、
                    描述感兴趣物体或现象随时间变化的特征，并定量分析、确定其变化的理论和方法。
                </div>
                <div class="con">
                    <div class="one">
                        <span>变化区域个数：</span>
                        <span>{{showData.length ? showData[current].nums : ''}}</span>
                    </div>
                    <div class="two">
                        <span>是否显示变化区域：</span>
                        <div class="eyes" @click="changeeyes">
                            <img src="../../../assets/eyes.svg" alt="" v-if="openeyes">
                            <img src="../../../assets/closeeyes.svg" alt="" v-else>
                        </div>
                    </div>
                    <div class="three">
                        <span>描边：</span>
                        <span class="color"></span>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
    import {changedetectionExample} from '@/api'
    export default {
        name: 'CDdetail',
        props: ['img1', 'img2', 'resimg1', 'resimg2', 'resnums'],
        watch: {
            resimg1: {
                immediate: true,
                handler(){
                    if (this.resimg1) {
                        const len = this.showData.length
                        if (len === 5) {
                            this.showData.unshift({
                                resimg1: this.img1, 
                                resimg2: this.img2,
                                resimg4: this.resimg1,
                                resimg5: this.resimg2,
                                nums: this.resnums
                            })
                        } else {
                            this.showData[0] = {
                                resimg1: this.img1, 
                                resimg2: this.img2,
                                resimg4: this.resimg1,
                                resimg5: this.resimg2,
                                nums: this.resnums
                            }
                        }
                    }
                }
            }
        },
        data() {
            return {
                openeyes: true,
                current: 0,
                showData: [],
            }
        },
        methods: {
            returnHome(){
                this.$parent.isDetail = false
            },
            // 40  664
            setLine(left){
                if (left >= 40 && left <= 664) {
                    this.$refs.line.style.left = left + 'px'
                    this.$refs.imgup.style.width = left + 'px'
                }     
            },
            returnMain() {
                this.$parent.isDetail = false
                this.$router.push({path: '/home'})
            },
            changeeyes() {
                this.openeyes = ! this.openeyes
            },
            changeCurrent(index) {
                this.current = index
            }
        },
        mounted() {     
            changedetectionExample().then((res) => {
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
        }
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

    .bolef{
        position: absolute;
        top: 0;
        left: 0;
        width: 400px;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        .tit {
            width: 100%;
            height: 40px;
            position: absolute;
            top: 6px;
            left: 0;
            color: white;
            line-height: 40px;
            text-align: center;
            font-size: 20px;
            font-weight: 700;
        }
        .con {
            width: 350px;
            height: 620px;
            overflow-y: auto;
            padding: 5px 15px;
            &::-webkit-scrollbar {
                display: none;
            }
            .item {
                // background: rgba(0, 0, 0, .2);
                width: 320px;
                height: 160px;
                margin-bottom: 70px;
                position: relative;
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
                    width: 100%;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    img {
                        width: 136px;
                        height: 136px;
                        &:nth-child(1) {
                            margin-right: 17px;
                        }
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

    .borig {
        position: absolute;
        top: 0;
        right: 0;
        width: 400px;
        height: 100%;
        justify-content: center;
        display: flex;
        flex-wrap: wrap;
        .con {
            width: 270px;
            height: 150px;
            border-radius: 8px;
            color: #abd4fd;
            background-color: #0F3A65;
            padding: 24px 19px;
            transform: translateY(-20px);
            .one {
                width: 100%;
                height: 35px;
                display: flex;
                justify-content: space-between;
                font-size: 17px;
            }
            .two {
                width: 100%;
                height: 35px;
                display: flex;
                justify-content: space-between;
                font-size: 17px;
                .eyes {
                    width: 24px;
                    height: 24px;
                    img {
                        width: 100%;
                        height: 100%;
                    }
                }
            }
            .three {
                width: 100%;
                height: 35px;
                display: flex;
                justify-content: space-between;
                font-size: 17px;
                .color {
                    width: 45px;
                    height: 24px;
                    background-color: rgb(0,255,127);
                }
            }
        }
        .describute {
            width: 270px;
            height: 350px;
            margin-top: 50px;
            border-radius: 8px;
            color: white; //#abd4fd
            background-color: #0F3A65;
            padding: 10px 15px;
        }
    }
</style>